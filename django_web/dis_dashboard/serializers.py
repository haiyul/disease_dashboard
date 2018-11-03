
from .models import *
from rest_framework import serializers


class AggTbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AggTb
        fields = ('year', 'month', 'reg_id', 'dis_id', 'agg_id', 'gd_id',
                  'case_num', 'dea_num', 'inci_rate', 'mort_rate')
