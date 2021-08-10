import requests
import json
from template import bill_database_template

base_url = "https://api.notion.com"

with open("conf.json", 'r') as f:
    config = json.load(f)
    secret_key = config["user_config"]["secret"]

headers = {
    "Notion-Version": "2021-07-27",
    "Authorization": "Bearer %s" % secret_key,
}


def create_page(body):
    url = base_url + "/v1/pages"

    response = requests.post(url, headers=headers, json=body)
    print(response.text)

    response_dict = json.loads(response.text)

    return response_dict.get("id")


def get_page_info(page_id: str) -> None:
    url = base_url + "/v1/pages/%s" % page_id
    response = requests.get(url, headers=headers)

    print(response.text)


def get_database_info(database_id: str) -> None:
    url = base_url + "/v1/databases/%s" % database_id
    response = requests.get(url, headers=headers)

    print(response.text)


def get_block_info(block_id: str) -> None:
    url = base_url + "/v1/blocks/%s" % block_id
    response = requests.get(url, headers=headers)

    print(response.text)


def query_database(database_id: str):
    url = base_url + "/v1/databases/%s/query" % database_id
    response = requests.post(url, headers=headers)

    print(response.text)


def create_database(body):
    url = base_url + "/v1/databases"

    response = requests.post(url, headers=headers, json=body)
    print(response.text)

    response_dict = json.loads(response.text)

    return response_dict.get("id")


if __name__ == '__main__':
    print(headers)
    create_database(bill_database_template.get_template("202107", "4401b02f36d24bd39db9d3df9b70d0d2"))

