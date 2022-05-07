import boto3
import requests


class Egoclient():

    def __init__(self,url = None):
        self.url =  "https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql"

        # with open("payload.txt","w") as f :
        #     f.write("{\"query\":\"{listSubscriptions(filter : {from_date: {eq: \\\"2022-04-27\\\"},to_date: {eq: \\\"2022-04-27\\\"},, status: {eq: \\\"A\\\"}, itemperpage: {eq: 10}, pagenumber: {eq: 0}}){\\n item_count\\n items{\\n L_balance\\n B_balance\\n D_balance\\n paid_amount\\n status\\n customer {\\n display_name\\n id\\n mobile\\n name\\n status\\n upd_by\\n upd_on\\n }\\n finish_date\\n id\\n product {\\n category\\n display_name\\n status\\n sale_price\\n name\\n id\\n }\\n start_date\\n upd_by\\n upd_on\\n cartitem_id\\n cart_id\\n orderscount {\\n meal_type\\n meals_consumed\\n meals_ordered\\n meals_remaining\\n meals_pausedORcancelled\\n }\\n }\\n }\\n }\\n\",\"variables\":{}}")
        self.read_file()

    def login(self,username= None,password=None):
        if username is None or password is None:
            return "please provide [username] and [password]"
        elif len(username) == 0 or len(password) == 0:
            return "please provide valid [username] and [password]"
        else:
            client = boto3.client('cognito-idp',region_name='us-east-1')
            response = client.initiate_auth(
                ClientId ='2m2s4a2m2cn62pb6jfhrarqju1',
                AuthFlow ='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME' :  username #'vltest1@gmail.com',
                    ,'PASSWORD' :  password #'Test@1234'
                }
            )
            self.accesstoken = response['AuthenticationResult']['AccessToken']
            self.key = 'authorization'

            return self.post()

    def read_file(self):
        with open("payload.txt",'r') as f:
            self.query = f.read()
 

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