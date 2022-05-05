import requests

class Egoclient():

    def __init__(self):
        self.url =  "https://ca57f53chjghzmmjskz3e6sptq.appsync-api.us-east-1.amazonaws.com/graphql"

        self.headers = {
        'x-api-key': 'da2-orjjngnz3ffc3jjnn75bfm4roi',
        'Content-Type': 'application/json'
        }

        # with open("payload.txt",'r') as f:
        #     self.query = f.read()
        self.query = "{\"query\":\"{\\n listItemCategories(limit:1000) {\\n items {\\n id\\n name\\n display_name\\n description\\n status\\n upd_by\\n upd_on\\n }\\n }\\n }\",\"variables\":{}}"

    def post(self):
        items = requests.post(url = self.url ,headers = self.headers, data = self.query )
        # return f"items : {items.text}"
        # print(items)
        # print(items.apparent_encoding)
        # print(items.close)
        # print(items.connection)
        # # print(items.content)
        # # print(items.text)
        # print(items.encoding)
        # print(items.headers)
        # print(items.cookies)
        # print(items.json())
        print(items.content)
    def login(self):
        pass

a = Egoclient()
a.post()

