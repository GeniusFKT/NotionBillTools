def get_template(title_text: str, parent_page_id: str):
    page = {
        "title": [
            {
                "type": "text",
                "text": {
                    "content": title_text,
                },
                "plain_text": title_text,
            }
        ],
        "properties": {
            "收/支": {
                "name": "收/支",
                "type": "select",
                "select": {
                    "options": []
                }
            },
            "交易类型": {
                "name": "交易类型",
                "type": "select",
                "select": {
                    "options": []
                }
            },
            "交易时间": {
                "name": "交易时间",
                "type": "date",
                "date": {}
            },
            "金额(元)": {
                "name": "金额(元)",
                "type": "number",
                "number": {
                    "format": "number"
                }
            },
            "交易对方": {
                "name": "交易对方",
                "type": "rich_text",
                "rich_text": {}
            },
            "商品": {
                "id": "title",
                "name": "商品",
                "type": "title",
                "title": {}
            },
            "交易平台": {
                "name": "交易平台",
                "type": "select",
                "select": {
                    "options": []
                }
            }
        },
        "parent": {
            "type": "page_id",
            "page_id": parent_page_id
        }
    }

    return page


def get_bill_item_template(database_id: str, start_date: str, income: str, bill_type: str, money: float, who: str,
                           product: str, platform: str):
    body = {
        "parent": {
            "type": "database_id",
            "database_id": database_id
        },
        "properties": {
            "交易时间": {
                "type": "date",
                "date": {
                    "start": start_date
                }
            },
            "收/支": {
                "type": "select",
                "select": {
                    "name": income,
                }
            },
            "交易类型": {
                "type": "select",
                "select": {
                    "name": bill_type,
                }
            },
            "交易平台": {
                "type": "select",
                "select": {
                    "name": platform,
                }
            },
            "金额(元)": {
                "type": "number",
                "number": money
            },
            "交易对方": {
                "type": "rich_text",
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": who,
                        },
                        "plain_text": who,
                    }
                ]
            },
            "商品": {
                "id": "title",
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": product,
                        },
                        "plain_text": product,
                    }
                ]
            }
        },
    }

    return body
