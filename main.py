import requests
import json
url_book = 'https://22dd1f97-419f-4670-90fe-b2048616ab91.mock.pstmn.io/book'
response = requests.get(url_book)
print(response.json())
url_auth = 'https://22dd1f97-419f-4670-90fe-b2048616ab91.mock.pstmn.io/auth'
data = {
    "login":"iddqd",
    "password":"qwerty"
}
response = requests.post(url_auth,json=data)
with open('log.json','w') as json_file:
    json.dump(response.json(),json_file)
with open('log.json','r') as json_file:
   print(json.load(json_file))