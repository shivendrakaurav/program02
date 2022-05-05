import requests


class get_method():
    def __init__(self):
        self.url = 'https://api.github.com/events'
    
    def get(self):
        r = requests.get(self.url)
        return r.text

a = get_method()
print(a.get())


class get_method():
    def __init__(self):

        self.url = "http://maps.googleapis.com/maps/api/geocode/json"


    def get(self):
        location = "delhi technological university"  
        r = requests.get(url = self.url, params = {'address':location})
  
        return  r.json()
  
a = get_method()
print(a.get())



class get_menthod():

    def __init__(self):
        self.url = 'https://w3schools.com/python/demopage2.php'
        
    def get(self):
        r = requests.post('https://httpbin.org/post', data={'key': 'value'})
        r = requests.put('https://httpbin.org/put', data={'key': 'value'})
        r = requests.delete('https://httpbin.org/delete')
        r = requests.head('https://httpbin.org/get')
        r = requests.options('https://httpbin.org/get')
        return r.content

a = get_menthod()
print(a.get())

class get_menthod():

    def __init__(self):
        self.url = 'https://w3schools.com/python/demopage2.php'
        
    def get(self):
        x = requests.get(self.url, cookies = {"favcolor": "Red"})
        return x.text

a = get_menthod()
print(a.get)


url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.content)



x = requests.get('https://daily.vibrantliving.in/')
print(x.status_code)

x = requests.get('https://daily.vibrantliving.in/')
print(x.content)

x = requests.get('https://daily.vibrantliving.in/')
print(x.text)

x = requests.get('https://w3schools.com')
print(x.content)