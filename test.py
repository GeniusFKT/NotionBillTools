import requests
import json

base_url = "https://api.notion.com"

headers = {
    "Notion-Version": "2021-07-27",
    "Authorization": "Bearer secret_Gf9qDfuNENFITYxhgwW5ffdDdmN24fkcYf0FmdwMO6y",
}

# url = base_url + "/v1/pages/Personal-Home-a93dda777d73478aae71b90751f5c995"
url = base_url + "/v1/users"
response = requests.get(url, headers=headers)

print(response.text)
