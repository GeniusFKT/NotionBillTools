import datetime
import os
import csv
import calendar

from template import bill_database_template
from utils import notion_api

# 路径
PROJECT_PATH = os.path.dirname(os.path.abspath('__file__'))
BILL_PATH = os.path.join(PROJECT_PATH, "bills")

# 获取时间信息
current_date = datetime.datetime.now().date()
this_month_start = datetime.datetime(current_date.year, current_date.month, 1)
this_month_end = datetime.datetime(current_date.year, current_date.month, calendar.monthrange(current_date.year, current_date.month)[1])

start = this_month_start.strftime("%Y%m%d")
end = this_month_end.strftime("%Y%m%d")

# 根据时间获取文件名
# file_name = "微信支付账单(%s-%s).csv" % (start, end)
file_name = "微信支付账单(%s-%s).csv" % ("20210701", "20210731")
file_path = os.path.join(BILL_PATH, file_name)


def get_wechat_bill(database_id: str):
    with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
        lines = f.readlines()
        striped_lines = []
        flag = False

        # 去除csv的开头信息部分，留下交易数据并导入字典中
        for line in lines:
            if not flag:
                if line.startswith("----------------------"):
                    flag = True
                continue
            striped_lines.append(line.strip())

        csv_reader = csv.DictReader(striped_lines)

        for row in csv_reader:
            # get datetime object from str
            start_date = datetime.datetime.fromisoformat(row.get("交易时间"))
            start_date = start_date.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
            start_date_iso_format = start_date.isoformat()

            income = row.get("收/支")
            bill_type = row.get("交易类型")
            # money example: "¥2000.00"
            money = float(row.get("金额(元)")[1:])

            # 支出取负
            if bill_type == "支出":
                money = -money

            who = row.get("交易对方")
            product = row.get("商品")

            body = bill_database_template.get_bill_item_template(database_id, start_date_iso_format, income, bill_type,
                                                                 money, who, product, "微信")
            notion_api.create_page(body)


if __name__ == '__main__':
    get_wechat_bill()
