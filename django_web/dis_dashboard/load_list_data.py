import csv
from dis_dashboard.models import *


# def run():
    # path = r'need_data/agg_code.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / n_row)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = AggCode(
    #             agg_id=row["agg_id"],
    #             ag_g=row["ag_g"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
    #
    # path = r'need_data/agg_tb.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / 100)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = AggTb(
    #             year=row["year"],
    #             month=row["month"],
    #             reg_id=row["reg_id"],
    #             dis_id=row["dis_id"],
    #             agg_id=row["agg_id"],
    #             gd_id=row["gd_id"],
    #             case_num=row["case_num"],
    #             dea_num=row["dea_num"],
    #             inci_rate=row["inci_rate"],
    #             mort_rate=row["mort_rate"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
    #
    # path = r'need_data/dis_code.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / n_row)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = DisCode(
    #             dis_id=row["dis_id"],
    #             dis_name=row["dis_name"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
    #
    # path = r'need_data/gd_code.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / n_row)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = GdCode(
    #             gd_id=row["gd_id"],
    #             gender=row["gender"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
    #
    # path = r'need_data/month_code.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / n_row)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = MonthCode(
    #             month=row["month"],
    #             month_cn=row["month_cn"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
    #
    # path = r'need_data/pro_code.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / n_row)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = ProCode(
    #             pro_name=row["pro_name"],
    #             pro_id=row["pro_id"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
    #
    # path = r'need_data/pro_tb.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / 100)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = ProTb(
    #             year=row["year"],
    #             month=row["month"],
    #             reg_id=row["reg_id"],
    #             dis_id=row["dis_id"],
    #             pro_name=row["pro_name"],
    #             case_num=row["case_num"],
    #             dea_num=row["dea_num"],
    #             inci_rate=row["inci_rate"],
    #             mort_rate=row["mort_rate"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
    #
    # path = r'need_data/reg_code.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / n_row)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = RegCode(
    #             reg_id=row["reg_id"],
    #             reg_name=row["reg_name"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
    #
    # path = r'need_data/reg_tb.csv'
    # n_row = len(list(csv.reader(open(path))))
    # split = int(n_row / 100)
    # split_list = range(0, n_row, split)
    # print(split_list)
    # count = 0
    # with open(path) as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         p = RegTb(
    #             year=row["year"],
    #             month=row["month"],
    #             reg_id=row["reg_id"],
    #             dis_id=row["dis_id"],
    #             case_num=row["case_num"],
    #             dea_num=row["dea_num"],
    #             inci_rate=row["inci_rate"],
    #             mort_rate=row["mort_rate"]
    #         )
    #         p.save()
    #         # print(row)
    #         if count in split_list:
    #             print(count / n_row)
    #             print(row)
    #         count = count + 1
