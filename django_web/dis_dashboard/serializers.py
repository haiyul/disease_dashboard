from .models import *
from rest_framework import serializers


class AggTbSerializer(serializers.HyperlinkedModelSerializer):
    month_cn = serializers.CharField(source='month.month_cn')
    reg_name = serializers.CharField(source='reg_id.reg_name')

    class Meta:
        model = AggTb
        fields = ('year', 'month_cn', 'reg_name', 'dis_id', 'agg_id', 'gd_id',
                  'case_num', 'dea_num', 'inci_rate', 'mort_rate')

