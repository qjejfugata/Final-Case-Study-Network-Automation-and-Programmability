import requests
import json

baseUrl = "http://localhost:59000/api/v1/api/v1"


headers = { "Content-type": "application/json"}

data = json.dumps({"username": "cisco", "password": "cisco123!"})

resp = requests.post(baseUrl+"/ticket", data=data,headers= headers)
print(baseUrl)
print(resp.status_code)
result = resp.json()
print(result)

ticket = result["response"]["serviceTicket"]
print(ticket)