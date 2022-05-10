from lib2to3.pgen2 import token
import requests
import srp
import json

class Egoclient():

    def __init__(self,url = None):
        self.url =  "https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql"

        with open("payload.txt","w") as f :
            f.write("{\"query\":\"{listSubscriptions(filter : {from_date: {eq: \\\"2022-04-27\\\"},to_date: {eq: \\\"2022-04-27\\\"},, status: {eq: \\\"A\\\"}, itemperpage: {eq: 10}, pagenumber: {eq: 0}}){\\n item_count\\n items{\\n L_balance\\n B_balance\\n D_balance\\n paid_amount\\n status\\n customer {\\n display_name\\n id\\n mobile\\n name\\n status\\n upd_by\\n upd_on\\n }\\n finish_date\\n id\\n product {\\n category\\n display_name\\n status\\n sale_price\\n name\\n id\\n }\\n start_date\\n upd_by\\n upd_on\\n cartitem_id\\n cart_id\\n orderscount {\\n meal_type\\n meals_consumed\\n meals_ordered\\n meals_remaining\\n meals_pausedORcancelled\\n }\\n }\\n }\\n }\\n\",\"variables\":{}}")
        self.read_file()


    def login(self,username= None,password=None):
        if username is None or password is None:
            return "please provide [username] and [password]"
        elif len(username) == 0 or len(password) == 0:
            return "please provide valid [username] and [password]"
        else:
            srp_token = self.srp_A() 
            response_first_call = self.first_request_call(srp_token)
            response_second_call = self.second_request_call(response_first_call['ChallengeParameters']['SECRET_BLOCK'])

            print(response_first_call['ChallengeParameters']['SECRET_BLOCK'])

            # print(srp_token)    
            # items = requests.post(url = self.url ,headers = self.header, data = self.payload)
            # print(f"items : {items.content}")


            # self.key = 'authorization'
            # return self.post()

    def read_file(self):
        with open("payload.txt",'r') as f:
            self.query = f.read()
 
    def srp_A(self) :

        # salt, vkey = srp.create_salted_verification_key( 'vltest1@gmail.com', 'Test@1234'  )
        usr      = srp.User( 'vltest1@gmail.com', 'Test@1234' )
        uname, token = usr.start_authentication()
        return token.hex()

    def first_request_call(self,srp_value):
        url = "https://cognito-idp.us-east-1.amazonaws.com/"
        headers = {
            "authority": "cognito-idp.us-east-1.amazonaws.com",
            "content-type" : "application/x-amz-json-1.1",
            "x-amz-target" : "AWSCognitoIdentityProviderService.InitiateAuth"
        }

        data = {"AuthFlow":"USER_SRP_AUTH",
        "AuthParameters":{"USERNAME":"vltest1@gmail.com",
        "SRP_A":srp_value},"ClientMetadata":{},
        "ClientId":"2m2s4a2m2cn62pb6jfhrarqju1"}
        data = json.dumps(data)
        response = requests.post(url, headers=headers, data=data)
        return response.json()



    def second_request_call(self,secret_block):
        url = "https://cognito-idp.us-east-1.amazonaws.com/"

        headers = {
            "authority": "cognito-idp.us-east-1.amazonaws.com",
            "content-type": "application/x-amz-json-1.1",
            "x-amz-target": "AWSCognitoIdentityProviderService.RespondToAuthChallenge"
        }

        data = {
            "ChallengeName": "PASSWORD_VERIFIER", 
            "ChallengeResponses":{"USERNAME": "04f4f5d9-1231-4b01-b746-6d87e767f744",
            "PASSWORD_CLAIM_SECRET_BLOCK": secret_block,
            "PASSWORD_CLAIM_SIGNATURE": "CadbB/CtccpFUl1ryBF7h9P+BWt6T1hfzrplOYTthPo=",
            "ClientId": "2m2s4a2m2cn62pb6jfhrarqju1",
            ClientMetadata: {}

            }

        }


        print(secret_block)


    def headers(self):
        headers ={self.key: self.accesstoken
                    ,'content-type': 'application/json'
        }  
        return headers

    def post(self):
        items = requests.post(url = self.url ,headers = self.headers(), data = self.query )
        return f"items : {items.text}"
    
    
    def list_items(self):
        self.url =  "https://ca57f53chjghzmmjskz3e6sptq.appsync-api.us-east-1.amazonaws.com/graphql"
        self.query = "{\"query\":\"{\\n listItemCategories(limit:1000) {\\n items {\\n id\\n name\\n display_name\\n description\\n status\\n upd_by\\n upd_on\\n }\\n }\\n }\",\"variables\":{}}"
        self.key = 'x-api-key'
        self.accesstoken =  'da2-orjjngnz3ffc3jjnn75bfm4roi'
        return self.post()



def validate_args(argv_list):

    if (len(argv_list) == 2):

        if argv_list[1] not in ("list_items","subscription") :
            raise Exception(f"{argv_list[1]}: incorrect operation name ")
    else:
        raise Exception("Usage: python subscription.py subscription/list_items")