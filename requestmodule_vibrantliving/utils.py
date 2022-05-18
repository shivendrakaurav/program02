import requests
import json
import sys, os, base64, datetime, hashlib, hmac 
from pycognito import aws_srp
import time


def generate_token(username = None,password=None):
        srp_token = srp_A(username,password) 
        response_first_call = first_request_call(srp_token)
        response_second_call = second_request_call(response_first_call)
        return response_second_call["AuthenticationResult"]["AccessToken"]

def srp_A(self) :

    aws = aws_srp.AWSSRP(
    username=self.username,
    password=self.password,
    pool_id='us-east-1_LmIBVgrWX',
    client_id='1elqc1ok4eqb1c9sjlhhiq74sd',
    pool_region='us-east-1'
    )

    srp_a = aws.get_auth_params()['SRP_A']
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
