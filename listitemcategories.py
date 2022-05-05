import requests

class Egoclient():

    def __init__(self):
        self.url =  "https://ca57f53chjghzmmjskz3e6sptq.appsync-api.us-east-1.amazonaws.com/graphql"

        self.headers = {
        'x-api-key': 'da2-orjjngnz3ffc3jjnn75bfm4roi',
        'Content-Type': 'application/json'
        }
        
        with open("payload.txt",'r') as f:
            self.query = f.read()
       

    def post(self):
        items = requests.post(url = self.url ,headers = self.headers, data = self.query )
        print(items.content)

        with open("L3.txt", 'wb') as fd:
            for chunk in items.iter_content(chunk_size=100):
                fd.write(chunk)
                fd.write(b"\n")

        

    def login(self):
        pass

a = Egoclient()
print(a.post())

