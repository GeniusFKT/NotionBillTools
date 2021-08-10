import datetime
import csv

from template import bill_database_template
from utils import notion_api


def get_wechat_bill(database_id: str, wechat_file_path: str):
    with open(wechat_file_path, "r", encoding="utf-8-sig", newline="") as f:
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
            if income == "支出":
                money = -money

            who = row.get("交易对方")
            product = row.get("商品")

            body = bill_database_template.get_bill_item_template(database_id, start_date_iso_format, income, bill_type,
                                                                 money, who, product, "微信")
            notion_api.create_page(body)
