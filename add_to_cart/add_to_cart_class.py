from lib2to3.pgen2 import token
import requests
import srp
import json
import sys, os, base64, datetime, hashlib, hmac 
from pycognito import aws_srp


class Egoclient(): 

    def __init__(self):
        self.url =  "https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql"
        # with open("payload.txt","w") as f :
        #     f.write("{\"query\":\"{listSubscriptions(filter : {from_date: {eq: \\\"2022-04-27\\\"},to_date: {eq: \\\"2022-04-27\\\"},, status: {eq: \\\"A\\\"}, itemperpage: {eq: 10}, pagenumber: {eq: 0}}){\\n item_count\\n items{\\n L_balance\\n B_balance\\n D_balance\\n paid_amount\\n status\\n customer {\\n display_name\\n id\\n mobile\\n name\\n status\\n upd_by\\n upd_on\\n }\\n finish_date\\n id\\n product {\\n category\\n display_name\\n status\\n sale_price\\n name\\n id\\n }\\n start_date\\n upd_by\\n upd_on\\n cartitem_id\\n cart_id\\n orderscount {\\n meal_type\\n meals_consumed\\n meals_ordered\\n meals_remaining\\n meals_pausedORcancelled\\n }\\n }\\n }\\n }\\n\",\"variables\":{}}")
        self.read_file()
        # self.username = username 
        # self.password = password



    def add_to_cart(self,username= None,password=None):
        self.username = username
        self.password = password

        if username is None or password is None:
            return "please provide [username] and [password]"        
        else:
            srp_token = self.srp_A() 
            response_first_call = self.first_request_call(srp_token)
            response_second_call = self.second_request_call(response_first_call)

            # print(response_first_call['ChallengeParameters']['SECRET_BLOCK'])
            # self.accesstoken = response_second_call["AuthenticationResult"]["AccessToken"]
            self.key = 'authorization'

                        
            # return self.post()

    def read_file(self):
        with open("payload.txt",'r') as f:
            self.query = f.read()
 
    def srp_A(self,username = None, password = None ) :

        # salt, vkey = srp.create_salted_verification_key( 'vltest1@gmail.com', 'Test@1234'  )
        self.aws = aws_srp.AWSSRP(
        username=username,
        password=password,
        pool_id='us-east-1_e5uzGdrC6',
        client_id='2m2s4a2m2cn62pb6jfhrarqju1',
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
        "ClientId":"1elqc1ok4eqb1c9sjlhhiq74sd",
        "AuthParameters":{"USERNAME":self.username,
        "SRP_A":srp_value}
        }
        data = json.dumps(data)

        response = requests.post(url, headers=headers, data=data)
        print(f"response : {response.status_code}")
        return response.json()


    def second_request_call(self,response):               
       
        # print(f"response : {response}")
        srp_b = int(response['ChallengeParameters']['SRP_B'],16)
        salt = response['ChallengeParameters']['SALT']
        user_id_for_srp = response['ChallengeParameters']['USER_ID_FOR_SRP']
        secret_key = response['ChallengeParameters']['SECRET_BLOCK']
        user_name = response['ChallengeParameters']['USERNAME']
        time_stamp = datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
        user_pool_id = 'us-east-1_LmIBVgrWX'
        # password = "SHiv#1234"

        # print(f"srp_b : {srp_b}")


        secret_key_bytes = base64.standard_b64decode(secret_key)
        msg = bytearray(user_pool_id.split('_')[1], 'utf-8') + bytearray(user_id_for_srp, 'utf-8') + \
        bytearray(secret_key_bytes) + bytearray(time_stamp, 'utf-8')    

        hkdf = self.aws.get_password_authentication_key(user_id_for_srp,self.password,srp_b, salt)
        hmac_obj = hmac.new(hkdf, msg, digestmod=hashlib.sha256)
        pass_claim_signature = base64.standard_b64encode(hmac_obj.digest())
        # print(f"signature string = {pass_claim_signature}")
 
        url = "https://cognito-idp.us-east-1.amazonaws.com/"

        headers = {
            "content-type": "application/x-amz-json-1.1",
            "x-amz-target": "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
        }

        paylaod = { 
            "ChallengeName": "PASSWORD_VERIFIER", 
            "ClientId": "1elqc1ok4eqb1c9sjlhhiq74sd",
            "ChallengeResponses":{"USERNAME": user_name ,
            "TIMESTAMP": time_stamp,
            "PASSWORD_CLAIM_SECRET_BLOCK": secret_key,
            "PASSWORD_CLAIM_SIGNATURE": pass_claim_signature.decode('utf-8'),
            } 
        }      

        paylaod = json.dumps(paylaod)
        response = requests.post(url, headers=headers, data=paylaod)
        response = response.json()
        # self.accesstoken = response["AuthenticationResult"]["AccessToken"]
        print(f"response : {response}")
        return response
        

    def headers(self):
        headers ={self.key: self.accesstoken
                    ,'content-type': 'application/json'
        }  
        return headers

    def post(self):
        items = requests.post(url = self.url ,headers = self.headers(), data = self.query )
        return f"items : {items.text}"
    
    
    # def list_items(self):
    #     self.url =  "https://ca57f53chjghzmmjskz3e6sptq.appsync-api.us-east-1.amazonaws.com/graphql"
    #     self.query = "{\"query\":\"{\\n listItemCategories(limit:1000) {\\n items {\\n id\\n name\\n display_name\\n description\\n status\\n upd_by\\n upd_on\\n }\\n }\\n }\",\"variables\":{}}"
    #     self.key = 'x-api-key'
    #     self.accesstoken =  'da2-orjjngnz3ffc3jjnn75bfm4roi'
    #     return self.post()

def validate_args(argv_list):

    if (len(argv_list) == 2):

        if argv_list[1] not in ("add_to_cart") :
            raise Exception(f"{argv_list[1]}: incorrect operation name ")
    else:
        raise Exception("Usage: python subscription.py add_to_cart")