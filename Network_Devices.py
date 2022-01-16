import requests
import json

baseUrl = "http://localhost:59000/api/v1/api/v1"
headers = { "Content-type": "application/json"}
data = json.dumps({"username": "cisco", "password": "cisco123!"})
resp = requests.post(baseUrl+"/ticket", data=data,headers= headers)

result = resp.json()

ticket = result["response"]["serviceTicket"]
headers = {"X-Auth-Token": ticket}

resp = requests.get(baseUrl+"/network-device", data=data,headers= headers)

print(resp.status_code)
result = resp.json()
print (json.dumps(result, indent=4))

for i in result["response"]:
    print(i["hostname"]+" "+i["serialNumber"]+" "+i["softwareVersion"])