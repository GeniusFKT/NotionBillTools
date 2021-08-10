import requests
import json
from template import bill_database_template

base_url = "https://api.notion.com"

headers = {
    "Notion-Version": "2021-07-27",
    "Authorization": "Bearer secret_Gf9qDfuNENFITYxhgwW5ffdDdmN24fkcYf0FmdwMO6y",
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
    # get_database_info("a878e26f4692414384cb10c66562ba36")
    # create_database(bill_database_template.get_template("111", "4401b02f36d24bd39db9d3df9b70d0d2"))
    query_database("a878e26f4692414384cb10c66562ba36")
