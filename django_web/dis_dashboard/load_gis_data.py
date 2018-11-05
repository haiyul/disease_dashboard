#用来从数据库里取数据
import os

from django.contrib.gis.utils import LayerMapping
from .models import *

# python manage.py shell
# from gis_sys import load_gis_data
# load_gis_data.run()
# quit()

provinceBorder_mapping = {
    'reg_id': 'reg_id',
    'name': 'NAME',
    'popname': 'POPNAME',
    'code': 'CODE',
    'type': 'TYPE',
    'display': 'DISPLAY',
    'x': 'X',
    'y': 'Y',
    'py': 'PY',
    'geom': 'POLYGON',
}


# 这是一个shp路径
provinceBorder_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'gis_data', 'province_border_union_single.shp'),
)


def run(verbose=True):
    lm = LayerMapping(
        ProvinceBorder, provinceBorder_shp, provinceBorder_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)



