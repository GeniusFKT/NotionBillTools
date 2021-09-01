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
                "select": {
                    "options": [
                        {
                            "name": "收入",
                            "color": "pink"
                        },
                        {
                            "name": "支出",
                            "color": "green"
                        }
                    ]
                }
            },
            "交易类型": {
                "select": {
                    "options": [
                        {
                            "name": "即时到账交易",
                            "color": "orange"
                        },
                        {
                            "name": "支付宝担保交易",
                            "color": "purple"
                        },
                        {
                            "name": "转账",
                            "color": "gray"
                        },
                        {
                            "name": "商户消费",
                            "color": "yellow"
                        },
                        {
                            "name": "扫二维码付款",
                            "color": "green"
                        }
                    ]
                }
            },
            "交易时间": {
                "date": {}
            },
            "金额(元)": {
                "number": {
                    "format": "yuan"
                }
            },
            "交易对方": {
                "rich_text": {}
            },
            "商品": {
                "title": {}
            },
            "交易平台": {
                "select": {
                    "options": [
                        {
                            "name": "支付宝",
                            "color": "blue"
                        },
                        {
                            "name": "微信",
                            "color": "green"
                        }
                    ]
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
            "database_id": database_id
        },
        "properties": {
            "交易时间": {
                "date": {
                    "start": start_date
                }
            },
            "收/支": {
                "select": {
                    "name": income,
                }
            },
            "交易类型": {
                "select": {
                    "name": bill_type,
                }
            },
            "交易平台": {
                "select": {
                    "name": platform,
                }
            },
            "金额(元)": {
                "number": money
            },
            "交易对方": {
                "rich_text": [
                    {
                        "text": {
                            "content": who,
                        },
                        "plain_text": who,
                    }
                ]
            },
            "商品": {
                "title": [
                    {
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
