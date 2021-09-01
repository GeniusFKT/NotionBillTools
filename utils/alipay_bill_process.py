import datetime
import csv

from template import bill_database_template
from utils import notion_api


def get_alipay_bill(database_id: str, alipay_file_path: str):
    with open(alipay_file_path, "r", encoding="gbk", newline="") as f:
        lines = f.readlines()
        striped_lines = []
        flag = False

        # 去除csv的开头/结尾信息部分，留下交易数据并导入字典中
        for line in lines:
            if not flag:
                if line.startswith("----------------------"):
                    flag = True
                continue

            if line.startswith("----------------------"):
                break
            # 由于alipay bill内字段可能包含多余的空格，由以下逻辑进行删除
            # split by ,
            text_list = line.strip().split(",")

            # delete abundant space
            text_list = list(map(lambda text: text.strip(), text_list))

            # join list to a string
            striped_lines.append(",".join(text_list))

        csv_reader = csv.DictReader(striped_lines)

        for row in csv_reader:
            # get datetime object from str
            # date could be ""
            start_date = row.get("付款时间")
            if start_date != "":
                start_date = datetime.datetime.fromisoformat(start_date)
                start_date = start_date.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
                start_date_iso_format = start_date.isoformat()
            else:
                start_date_iso_format = ""

            income = row.get("收/支")
            if income == "":
                income = "转账"
            bill_type = row.get("类型")
            # money example: "2000.00"
            money = float(row.get("金额（元）"))

            # 支出取负
            if income == "支出":
                money = -money

            who = row.get("交易对方")
            product = row.get("商品名称")

            body = bill_database_template.get_bill_item_template(database_id, start_date_iso_format, income, bill_type,
                                                                 money, who, product, "支付宝")
            notion_api.create_page(body)
