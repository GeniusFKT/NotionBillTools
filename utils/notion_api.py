import requests
import json
import os


# base api url
base_url = "https://api.notion.com"

# load secret key
secret_key = os.environ.get("NOTION_KEY")

headers = {
    "Notion-Version": "2021-08-16",
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
