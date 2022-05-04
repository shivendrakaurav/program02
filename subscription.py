import requests

class Egoclient():

    def __init__(self):
        self.url =  "https://4du5xi23jneq5gmwctl2vl42ty.appsync-api.us-east-1.amazonaws.com/graphql"
        self.headers ={'authorization': """eyJraWQiOiJDZ3oxaEh6ZXZvcGJzNjU3QjJuU3k0cTliMDJzUkcxZmE2a04rNHhpbFhNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIwNGY0ZjVkOS0xMjMxLTRiMDEtYjc0Ni02ZDg3ZTc2N2Y3NDQiLCJjb2duaXRvOmdyb3VwcyI6WyJhZG1pbiJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9lNXV6R2RyQzYiLCJjbGllbnRfaWQiOiIybTJzNGEybTJjbjYycGI2amZocmFycWp1MSIsIm9yaWdpbl9qdGkiOiJiOGU3MGFjYS1mOTNmLTRkNjItODYyNy00YjczYmQzNjZhMzQiLCJldmVudF9pZCI6ImIwNDMxZjkyLTM2YWUtNDRjZi04ODE5LTM1Y2M3NGFkYTkyNiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NTE2NTc4NTQsImV4cCI6MTY1MTY2ODExOCwiaWF0IjoxNjUxNjYwOTE5LCJqdGkiOiI1MTMxZTY2My1kM2QzLTRjYjEtYTVlNC1kYzdjMjZiZmNkOTUiLCJ1c2VybmFtZSI6IjA0ZjRmNWQ5LTEyMzEtNGIwMS1iNzQ2LTZkODdlNzY3Zjc0NCJ9.P66QS0RhZZz4HLHLv9nqFuiOmDKlYYQ4lVSM0XoRgLYi-1MyJGXVEyabJ5MBIcr1M94twWLmqtiiUn3CH9blnxfYK4QC2Ev8fIutvhnMuEXUxn2UsA5MI-rpME5x23H8sE03Rx33iopX3dU2E6vcH4CTSUqp9rW1_gnvLpO58cR9UaF4dYKRdK7m6LgTGCQca-L8G-Fuh9699ZvGiLaNhmm7Y3N8Fr1GeGQUq3_Y6JuDipBhzWpsoF0Ln7MGt6kRd2_jPqazMmJimGs9tbAtpfo-fYaMW0D0Tk0Dl6hagk9sGEleyJ6CzBina5gCMHDjQYpCpU44qA9aRAySzgpssw"""
                ,'content-type': 'application/json'
        }

        # with open("payload.txt",'r') as f:
        #     self.query = f.read()
        self.query =  "{\"query\":\"{listSubscriptions(filter : {from_date: {eq: \\\"2022-04-27\\\"},to_date: {eq: \\\"2022-04-27\\\"},, status: {eq: \\\"A\\\"}, itemperpage: {eq: 10}, pagenumber: {eq: 0}}){\\n item_count\\n items{\\n L_balance\\n B_balance\\n D_balance\\n paid_amount\\n status\\n customer {\\n display_name\\n id\\n mobile\\n name\\n status\\n upd_by\\n upd_on\\n }\\n finish_date\\n id\\n product {\\n category\\n display_name\\n status\\n sale_price\\n name\\n id\\n }\\n start_date\\n upd_by\\n upd_on\\n cartitem_id\\n cart_id\\n orderscount {\\n meal_type\\n meals_consumed\\n meals_ordered\\n meals_remaining\\n meals_pausedORcancelled\\n }\\n }\\n }\\n }\\n\",\"variables\":{}}"

    def post(self):
        items = requests.post(url = self.url ,headers = self.headers, data = self.query )
        return f"items : {items.text}"
    

    def login(self):
        pass

a = Egoclient()
print(a.post())

