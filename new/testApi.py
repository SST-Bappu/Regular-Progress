# import requests
# response = requests.get("https://mboum.com/api/v1/qu/quote/balance-sheet/?symbol=F")
# data = response.json()
# print(data)

import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

querystring = {"symbol":"AMRN","region":"US"}

headers = {
    'x-rapidapi-key': "82dc7a99d9msh52e3aeb7e8651d7p1cf0a6jsnb1154c537de1",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
for key in data:
    print(key)
print("------")
for key in data['earnings']:
    print(key)
print(data['details'])
