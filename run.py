import datetime

from template import bill_database_template
from utils import notion_api, wechat_bill_process, alipay_bill_process

PARENT_PAGE_ID = "4401b02f36d24bd39db9d3df9b70d0d2"
now = datetime.datetime.now()

format_date = now.strftime("%Y-%m")

if __name__ == '__main__':
    db_id = notion_api.create_database(bill_database_template.get_template("%s月度账单" % format_date, PARENT_PAGE_ID))
    alipay_bill_process.get_alipay_bill(db_id)
    wechat_bill_process.get_wechat_bill(db_id)
    print(db_id)
