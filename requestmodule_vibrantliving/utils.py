import requests
import json
import  os, base64, datetime, hashlib, hmac 
from pycognito import aws_srp
import os

def generate_token(username ,password):
    """takes username and password,generate access token and returns it
    py:function::

    Args:
        username(str),password(str): username and password to be used to generate access token using request calls

    Returns:
        response_second_call["AuthenticationResult"]["AccessToken"](str) : access token
    """
    aws,srp_token = srp_A(username,password) 
    response_first_call = first_request_call(srp_token,username)
    response_second_call = second_request_call(response_first_call,aws,password)
    # print(f"response : {response_second_call}")
    return response_second_call["AuthenticationResult"]["AccessToken"]

def srp_A(user,passw) :
    """takes username and password, calculates srp_a using AWSSRP and returns it
    py:function::

    Args:
        user(str),passw(str): user and passw used to generate srp_a

    Returns:
         aws(object),srp_a(str): aws object of user,passw and srp_a for the same 
    """

    aws = aws_srp.AWSSRP(
    username=user,
    password=passw,
    pool_id=os.environ['USER_POOLID'],
    client_id=os.environ['CLIENT_ID'],
    pool_region=os.environ['POOL_REGION']
    )

    srp_a = aws.get_auth_params()['SRP_A']
    return aws,srp_a

def first_request_call(srp_value,user):
    """takes srp_value and username,performs request operation and print the time taken for the operation, returns reponse of it  
    py:function::
    
    Args:
        srp_value(str),user(str): srp_value and user is used in payload

    Returns:
        response.json(json): returns reponse of request operation in json format 
    """
    url = "https://cognito-idp.us-east-1.amazonaws.com/"
    headers = {
        "content-type" : "application/x-amz-json-1.1",
        "x-amz-target" : "AWSCognitoIdentityProviderService.InitiateAuth"
    }

    data = {"AuthFlow":"USER_SRP_AUTH", 
    "AuthParameters":{"USERNAME":user,
    "SRP_A":srp_value},
    "ClientId": os.environ['CLIENT_ID']}
    data = json.dumps(data)

    response = requests.post(url, headers=headers, data=data)
    print(f"response : {response.status_code}")
    return response.json()

def second_request_call(response,aws,passw):
    """takes response and aws and passw, generate pass claim signature,performs request operation and returns it's response
    py:function::

    Args:
        response(json),passw(str): generate pass claim signature using input

    Returns:
        response.json(json):  response of request module
    """               
    
    srp_b = int(response['ChallengeParameters']['SRP_B'],16)
    salt = response['ChallengeParameters']['SALT']
    user_id_for_srp = response['ChallengeParameters']['USER_ID_FOR_SRP']
    secret_key = response['ChallengeParameters']['SECRET_BLOCK']
    user_name = response['ChallengeParameters']['USERNAME']
    time_stamp = datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
    user_pool_id = os.environ['USER_POOLID']
    password = passw

    secret_key_bytes = base64.standard_b64decode(secret_key)
    msg = bytearray(user_pool_id.split('_')[1], 'utf-8') + bytearray(user_id_for_srp, 'utf-8') + \
    bytearray(secret_key_bytes) + bytearray(time_stamp, 'utf-8')    

    hkdf = aws.get_password_authentication_key(user_id_for_srp,password,srp_b, salt)
    hmac_obj = hmac.new(hkdf, msg, digestmod=hashlib.sha256)
    pass_claim_signature = base64.standard_b64encode(hmac_obj.digest())
    
    url = "https://cognito-idp.us-east-1.amazonaws.com/"

    headers = {
        "content-type": "application/x-amz-json-1.1",
        "x-amz-target": "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
    }

    paylaod = { 
        "ChallengeName": "PASSWORD_VERIFIER", 
        "ClientId": os.environ['CLIENT_ID'],
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
    """takes argv_list,checks agrv correct format and returns exception if error occured otherwise True
    py:function::

    Args:
        argv_list(list): argv_list to validate

    Returns:
        True or exception : returns True or raise exception according to details

    """
    if (len(argv_list) == 2):
        if argv_list[1] in("cart_details","list_subscriptions","list_items","add_to_cart") :
            return True
        else:
            raise Exception(f"{argv_list[1]}: incorrect operation name")
    else:
        raise Exception("Usage: python main.py <cart_details/add_to_cart/list_subscriptions/list_items>")