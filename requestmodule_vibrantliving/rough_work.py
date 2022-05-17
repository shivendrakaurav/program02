
import requests
from pycognito.utils import RequestsSrpAuth

auth = RequestsSrpAuth(
  username='vltest1@gmail.com',
  password='Test@1234' ,
  user_pool_id='us-east-1_LmIBVgrWX',
  client_id="1elqc1ok4eqb1c9sjlhhiq74sd",
  user_pool_region='us-east-1',
)

response = requests.get('https://cognito-idp.us-east-1.amazonaws.com/', auth=auth)

