import csv
from dis_dashboard.models import *

path = r'data_normal/AreaList.csv'
with open(path) as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        row = row[0].split('\t')
        print(row)
        _, created = AreaList.objects.get_or_create(
            area_name=row[0],
            area_name_reg=row[1],
            area_name_short=row[2],
        )


path = r'data_normal/DisList.csv'
with open(path) as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        row = row[0].split('\t')
        print(row)
        _, created = DisList.objects.get_or_create(
            dis_name=row[0],
        )

