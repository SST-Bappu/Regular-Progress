import requests

response = requests.get('https://api.covid19api.com/countries').json()
print(response)
