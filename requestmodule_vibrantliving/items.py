import requests
import json
import sys, os, base64, datetime, hashlib, hmac 
from pycognito import aws_srp


class Egoclient(): 

    def __init__(self,username=None,password=None):
        self.username = username
        self.password = password
        self.clientid = "1elqc1ok4eqb1c9sjlhhiq74sd"
        self.userpoolid = "us-east-1_LmIBVgrWX"

        if sys.argv[1].lower() in ("list_items"):
            self.url = "https://ca57f53chjghzmmjskz3e6sptq.appsync-api.us-east-1.amazonaws.com/graphql"
        elif sys.argv[1].lower() in ("add_to_cart"):
            self.url = "https://m76jgm5mv5a5ta56kwht6e6ipm.appsync-api.us-east-1.amazonaws.com/graphql"
        else:
            self.url = "https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql"

    def add_to_cart(self):   
        self.accesstoken = self.generate_token()            
        self.content_type = '"text/plain;charset=UTF-8"'
        self.query =  "query ($customer_id: ID!){\n    listCarts(filter: {customer_id: {eq: $customer_id},pay_status:{eq:\"UNPAID\"}}) {\n    items {\n      customer_id\n      customer_mobile\n      customer_name\n      id\n      ciid\n      grand_total\n      pay_status\n      item {\n        defaultimg_url\n        item_name\n        tax_methods\n        uom_name\n        category\n        item_id\n        sub_total\n        qty\n        tax_amount\n        subscription {\n          address {\n            aline1\n            aline2\n            city\n            tag\n            landmark\n            postalcode\n          }\n          isDelivery\n          meal_type\n          notes\n          order_dates\n          sale_val\n        }\n        variants {\n          display_name\n          items {\n            display_name\n          }\n        }\n      }\n    }\n    grand_total\n  }\n}"
        payload = {
            "query" : self.query,
            "variables" :{"customer_id": "22906fac-fcfc-4016-b041-1b66171305c4"
            }
        }
        self.payload = json.dumps(payload)   
        self.key = 'authorization'                       
        return self.post()

    def generate_token(self):
        srp_token = self.srp_A() 
        response_first_call = self.first_request_call(srp_token)
        response_second_call = self.second_request_call(response_first_call)
        return response_second_call["AuthenticationResult"]["AccessToken"]

    def list_subscriptions(self):
        self.accesstoken = self.generate_token() 
        self.read_file()
        self.key = 'authorization' 
        self.content_type = 'application/json'
        return self.post()

    def read_file(self):
        with open("payload.txt",'r') as f:
            self.payload = f.read()
 
    def srp_A(self) :

        self.aws = aws_srp.AWSSRP(
        username=self.username,
        password=self.password,
        pool_id='us-east-1_LmIBVgrWX',
        client_id='1elqc1ok4eqb1c9sjlhhiq74sd',
        pool_region='us-east-1'
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

    def post(self):
        headers ={self.key: self.accesstoken
                    ,'content-type': self.content_type
        } 
        items = requests.post(url = self.url ,headers = headers, data = self.payload )
        return f"items : {items.content}"
    
    
    def list_items(self):
        self.payload = "{\"query\":\"{\\n listItemCategories(limit:1000) {\\n items {\\n id\\n name\\n display_name\\n description\\n status\\n upd_by\\n upd_on\\n }\\n }\\n }\",\"variables\":{}}"
        self.key = 'x-api-key'
        self.accesstoken =  'da2-orjjngnz3ffc3jjnn75bfm4roi'
        self.content_type = "application/json"
        return self.post()

def validate_args(argv_list):

    if (len(argv_list) == 2):
        if argv_list[1] not in ("add_to_cart","list_subscriptions","list_items") :
            raise Exception(f"{argv_list[1]}: incorrect operation name")
    else:
        raise Exception("Usage: python main.py <add_to_cart/list_subscriptions/list_items>")