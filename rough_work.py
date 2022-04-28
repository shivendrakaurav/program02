import requests
import json


class Egoclient():

    def __init__(self):
        self.url = "https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql"

        self.query =   "{\"query\":\"{listSubscriptions(filter : {from_date: {eq: \\\"2022-04-27\\\"},to_date: {eq: \\\"2022-04-27\\\"},, status: {eq: \\\"A\\\"}, itemperpage: {eq: 10}, pagenumber: {eq: 0}}){\\n item_count\\n items{\\n L_balance\\n B_balance\\n D_balance\\n paid_amount\\n status\\n customer {\\n display_name\\n id\\n mobile\\n name\\n status\\n upd_by\\n upd_on\\n }\\n finish_date\\n id\\n product {\\n category\\n display_name\\n status\\n sale_price\\n name\\n id\\n }\\n start_date\\n upd_by\\n upd_on\\n cartitem_id\\n cart_id\\n orderscount {\\n meal_type\\n meals_consumed\\n meals_ordered\\n meals_remaining\\n meals_pausedORcancelled\\n }\\n }\\n }\\n }\\n\",\"variables\":{}}"
        
        self.headers = {'authorization': 'eyJraWQiOiJDZ3oxaEh6ZXZvcGJzNjU3QjJuU3k0cTliMDJzUkcxZmE2a04rNHhpbFhNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxMzhlNzc2My0yZDEwLTQxYWUtYjBiYS1lNzZkZmYzMWU1ZjciLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9lNXV6R2RyQzYiLCJjbGllbnRfaWQiOiIybTJzNGEybTJjbjYycGI2amZocmFycWp1MSIsIm9yaWdpbl9qdGkiOiJiYTVhMDRhNC02M2JjLTQ4N2EtYTM0OC04M2Y0OTMwYzE5OGIiLCJldmVudF9pZCI6ImI4OWRjYTNhLTczNTQtNGIwMi05ODk2LTc4ZThkOTFjMDEwNiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTEwNjU1NTMsImV4cCI6MTY1MTA2NTg1MywiaWF0IjoxNjUxMDY1NTUzLCJqdGkiOiJkMDBhMDIwMS04ZDZmLTRjYzYtODVjOC03NDkwZGY4YmMxOTUiLCJ1c2VybmFtZSI6IjEzOGU3NzYzLTJkMTAtNDFhZS1iMGJhLWU3NmRmZjMxZTVmNyJ9.KAgVo4UJMJ6s4HQyHLOyEM9s7WWGk_SnqqfsWyduIosPXiYLPf5_yawSqzK36cz0X72M93dGzoSqHOzyX9kq3qA61uPjZGwc136nvRplcNXJMUEnj7BUm5YVRsARlaDCZnMgIGDduHj5imhZaq72pFAOAEiAThjBbW6uYuKfuakvnJs4eAV9wL_P6G2jrQVxFX4tDjUBT_x0YtdokcBby-Z4c5BciqakCstYpqbmZ1EaLOEfqVsY_1kOZThL3h8fo4URUN5Qsuii4oBlAbmoLIi1zFcLbcADQRhk8ZHENHZNWJfyXjXCAifW-FAoNMP_DCMsEbPHhen4lHKwkpUmew'
        ,'content-type': 'application/json'
        }
    def post(self):
        items = requests.post(url = self.url ,headers = self.headers, data = self.query )
        return f"items : {items.text}"
    
    def login(self):
        pass

a = Egoclient()
print(a.post())


# headers = {
# 'x-api-key': 'da2-orjjngnz3ffc3jjnn75bfm4roi',
# 'Content-Type': 'application/json'
# }
# query = "{\"query\":\"{\\n listItemCategories(limit:1000) {\\n items {\\n id\\n name\\n display_name\\n description\\n status\\n upd_by\\n upd_on\\n }\\n }\\n }\",\"variables\":{}}"

# print(dir(query))
# # var = {"game"  : "football",
# #     "conten-Type" : "application/json"
# #     }

# # print(dir(var))


