import requests
import json
import sys, os 
import time

class Egoclient(): 

    def __init__(self):
    
        self.clientid = os.environ['CLIENT_ID']                #storing client id in os 
        self.userpoolid = os.environ['USER_POOLID']            #storing userpool id in os
        self.customer_id = os.environ['CUSTOMER_ID']           #storing customer id in os
        self.pool_region = os.environ['POOL_REGION']           #storing pool regin in os

        #storing url in os
        if sys.argv[1].lower() in ("list_items"):
            self.url =  os.environ['LIST_ITEM_URL']
        elif sys.argv[1].lower() in ("cart_details","add_to_cart"):
            self.url = os.environ['CART_URL']
        else:
            self.url = os.environ['SUBSCRIPTION_URL']


    def cart_details(self,token):
        """takes access token and add payload,returns to post call
        py:function::

        Args:
            token(str) : token to be used in headers

        Returns:
            self.post(function): calls self.post() function
        """ 
        self.accesstoken = token        
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

    
    def add_to_cart(self,token):
        """takes token,add payload,calls self.post function and calculates its time to execute,returns customer details
        py:function::

        Args:
            token(str) : token to be used in headers

        Returns:
            customer_details(str) : customer details
        """
        self.accesstoken = token

        start = time.time()
        self.key = "authorization"
        self.content_type = "text/plain;charset=UTF-8"
        payload = {
            "query": "mutation ($input: CreateCartInput!){\n              createCart(input: $input) {\n                id\n                customer_id\n              }\n            }",
            "variables":{"input":{"customer_id":self.customer_id,"item":{"item_id":"7d721055-b8f9-45b0-b3b4-23e591d4e39b","qty":1,"subscription":[{"address":{},"addon_items":[],"isDelivery":False,"meal_type":"B","notes":"","order_dates":[]}],"variants":[{"display_name":"Duration","items":{"display_name":"1 day sampler"}}]}}}}

        self.payload = json.dumps(payload)
        customer_details = self.post()
        end = time.time()

        print(f"time taken to add items to cart: {end - start}") 
        return customer_details

    def list_subscriptions(self,token):
        """takes token,add payload,calls self.post function
        py:function::

        Args:
            token(str): token to be used in headers

        Returns:
            self.post(function): calls self.post function
        """
        self.accesstoken = token
        with open("subscription_payload.txt",'r') as f:
            self.payload = f.read()
        self.key = 'authorization' 
        self.content_type = 'application/json'
        return self.post()
    
    def list_items(self):
        """takes none,add payload and access token and headers details,calls self.post function
        py:function::

        Args:
            None
        
        Returns:
            self.post(function): calls self.post function
        """
        with open("list_payload.txt","r") as f :
            self.payload = f.read()
        
        self.key = 'x-api-key'
        self.accesstoken =  'da2-orjjngnz3ffc3jjnn75bfm4roi'
        self.content_type = "application/json"
        return self.post()

    def post(self):
        """takes None, performs request operation
        py:function::

        Args:
            None
        
        Returns:
            items.content(string): content of request operation
        """
        headers ={self.key: self.accesstoken
                    ,'content-type': self.content_type
        } 
        items = requests.post(url = self.url ,headers = headers, data = self.payload )
        return f"items : {items.content}"
