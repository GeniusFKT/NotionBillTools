import json
import os

from template import bill_database_template
from utils import notion_api, wechat_bill_process, alipay_bill_process

# get project path
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
CONF_PATH = os.path.join(PROJECT_PATH, "conf.json")

if __name__ == '__main__':
    # read config from conf.json
    with open(CONF_PATH, 'r') as f:
        config = json.load(f)
        print(config)

        parent_page_id = config["notion_config"]["parent_page_id"]
        title = config["notion_config"]["title"]
        bill_path = config["file_config"]["path"]
        wechat_file = config["file_config"]["bill_files"]["wechat"]
        alipay_file = config["file_config"]["bill_files"]["alipay"]

        # get file path
        project_bill_path = os.path.join(PROJECT_PATH, bill_path)
        wechat_file_path = os.path.join(project_bill_path, wechat_file)
        alipay_file_path = os.path.join(project_bill_path, alipay_file)

        # create database under parent page
        db_id = notion_api.create_database(bill_database_template.get_template(title, parent_page_id))

        # precess different bills
        alipay_bill_process.get_alipay_bill(db_id, alipay_file_path)
        wechat_bill_process.get_wechat_bill(db_id, wechat_file_path)
        print(db_id)
