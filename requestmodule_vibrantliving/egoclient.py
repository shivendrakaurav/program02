import requests
import json
import sys, os, base64, datetime, hashlib, hmac 
from pycognito import aws_srp
import time


class Egoclient(): 

    def __init__(self,username=None,password=None):
        self.username = username
        self.password = password
        self.clientid = os.environ['CLIENT_ID']                #storing client id in os 
        self.userpoolid = os.environ['USER_POOLID']            #storing userpool id in os
        self.customer_id = os.environ['CUSTOMER_ID']
        self.pool_region = os.environ['POOL_REGION']

        #storing url in os
        if sys.argv[1].lower() in ("list_items"):
            self.url =  os.environ['LIST_ITEM_URL']
        elif sys.argv[1].lower() in ("cart_details","add_to_cart"):
            self.url = os.environ['CART_URL']
        else:
            self.url = os.environ['SUBSCRIPTION_URL']


    def cart_details(self):   
        self.accesstoken = self.generate_token()        
        self.content_type = '"text/plain;charset=UTF-8"'        
        with open("cart_query.txt","r") as f:
            self.query = f.read()
        payload = {
            "query" : self.query,
            "variables" :{"customer_id": self.customer_id
            }
        }
        self.payload = json.dumps(payload)   
        self.key = 'authorization'                       
        return self.post()

    
    def add_to_cart(self):
        self.accesstoken = self.generate_token()

        start = time.time()
        self.key = "authorization"
        self.content_type = "text/plain;charset=UTF-8"
        payload = {
            "query": "mutation ($input: CreateCartInput!){\n              createCart(input: $input) {\n                id\n                customer_id\n              }\n            }",
            "variables":{"input":{"customer_id":self.customer_id,"item":{"item_id":"7d721055-b8f9-45b0-b3b4-23e591d4e39b","qty":1,"subscription":[{"address":{},"addon_items":[],"isDelivery":False,"meal_type":"B","notes":"","order_dates":[]}],"variants":[{"display_name":"Duration","items":{"display_name":"1 day sampler"}}]}}}}

        self.payload = json.dumps(payload)
        customer_details = self.post()
        end = time.time()

        print(f"addindg items to cart: {end - start}") 
        return customer_details

    def list_subscriptions(self):
        self.accesstoken = self.generate_token() 
        with open("subscription_payload.txt",'r') as f:
            self.payload = f.read()
        self.key = 'authorization' 
        self.content_type = 'application/json'
        return self.post()
    
    def list_items(self):
        with open("list_payload.txt","r") as f :
            self.payload = f.read()
        
        self.key = 'x-api-key'
        self.accesstoken =  'da2-orjjngnz3ffc3jjnn75bfm4roi'
        self.content_type = "application/json"
        return self.post()

    def post(self):
        headers ={self.key: self.accesstoken
                    ,'content-type': self.content_type
        } 
        items = requests.post(url = self.url ,headers = headers, data = self.payload )
        return f"items : {items.content}"

    def generate_token(self):
        srp_token = self.srp_A() 
        response_first_call = self.first_request_call(srp_token)
        response_second_call = self.second_request_call(response_first_call)
        return response_second_call["AuthenticationResult"]["AccessToken"]
 
    def srp_A(self) :

        self.aws = aws_srp.AWSSRP(
        username=self.username,
        password=self.password,
        pool_id=os.environ['USER_POOLID'],
        client_id=os.environ['CLIENT_ID'] ,
        pool_region=self.pool_region
        )

        srp_a =self.aws.get_auth_params()['SRP_A']
        return srp_a

    def first_request_call(self,srp_value):
        url = "https://cognito-idp.us-east-1.amazonaws.com/"
        headers = {
            "content-type" : "application/x-amz-json-1.1",
            "x-amz-target" : "AWSCognitoIdentityProviderService.InitiateAuth"
        }

        data = {"AuthFlow":"USER_SRP_AUTH", 
        "AuthParameters":{"USERNAME":self.username,
        "SRP_A":srp_value},
        "ClientId": self.clientid}
        data = json.dumps(data)

        response = requests.post(url, headers=headers, data=data)
        print(f"response : {response.status_code}")
        return response.json()

    def second_request_call(self,response):               
       
        srp_b = int(response['ChallengeParameters']['SRP_B'],16)
        salt = response['ChallengeParameters']['SALT']
        user_id_for_srp = response['ChallengeParameters']['USER_ID_FOR_SRP']
        secret_key = response['ChallengeParameters']['SECRET_BLOCK']
        user_name = response['ChallengeParameters']['USERNAME']
        time_stamp = datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
        user_pool_id = self.userpoolid
        password = self.password

        secret_key_bytes = base64.standard_b64decode(secret_key)
        msg = bytearray(user_pool_id.split('_')[1], 'utf-8') + bytearray(user_id_for_srp, 'utf-8') + \
        bytearray(secret_key_bytes) + bytearray(time_stamp, 'utf-8')    

        hkdf = self.aws.get_password_authentication_key(user_id_for_srp,password,srp_b, salt)
        hmac_obj = hmac.new(hkdf, msg, digestmod=hashlib.sha256)
        pass_claim_signature = base64.standard_b64encode(hmac_obj.digest())
        
        url = "https://cognito-idp.us-east-1.amazonaws.com/"

        headers = {
            "content-type": "application/x-amz-json-1.1",
            "x-amz-target": "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
        }

        paylaod = { 
            "ChallengeName": "PASSWORD_VERIFIER", 
            "ClientId": self.clientid,
            "ChallengeResponses":{"USERNAME": user_name ,
            "TIMESTAMP": time_stamp,
            "PASSWORD_CLAIM_SECRET_BLOCK": secret_key,
            "PASSWORD_CLAIM_SIGNATURE": pass_claim_signature.decode('utf-8'),
            } 
        }      

        paylaod = json.dumps(paylaod)
        response = requests.post(url, headers=headers, data=paylaod)
        print(f"response 2 : {response.status_code}")
        return response.json()


def validate_args(argv_list):

    if (len(argv_list) == 2):
        if argv_list[1] not in ("cart_details","list_subscriptions","list_items","add_to_cart") :
            raise Exception(f"{argv_list[1]}: incorrect operation name")
    else:
        raise Exception("Usage: python main.py <cart_details/add_to_cart/list_subscriptions/list_items>")