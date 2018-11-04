from .models import *
from rest_framework import serializers
import django_filters


# 年龄分组的表
# class AggTbSerializer(serializers.HyperlinkedModelSerializer):
class AggTbSerializer(serializers.ModelSerializer):
    month = serializers.CharField(source='month.month_cn')
    reg_name = serializers.CharField(source='reg_id.reg_name_crt')
    dis_name = serializers.CharField(source='dis_id.dis_name')
    ag_g_ctr = serializers.CharField(source='agg_id.ag_g_ctr')
    gender = serializers.CharField(source='gd_id.gender')

    class Meta:
        model = AggTb
        fields = ('year', 'month', 'reg_name', 'dis_name', 'ag_g_ctr', 'gender',
                  'case_num', 'dea_num', 'inci_rate', 'mort_rate')


# 筛选法则
class AggTbFilterSet(django_filters.FilterSet):
    month = django_filters.CharFilter(field_name='month__month_cn')
    reg_name = django_filters.CharFilter(field_name='reg_id__reg_name_crt')
    dis_name = django_filters.CharFilter(field_name='dis_id__dis_name')
    ag_g_ctr = django_filters.CharFilter(field_name='agg_id__ag_g_ctr')
    gender = django_filters.CharFilter(field_name='gd_id__gender')

    class Meta:
        model = AggTb
        fields = ['year', 'month', 'reg_name', 'dis_name', 'ag_g_ctr', 'gender',
                  'case_num', 'dea_num', 'inci_rate', 'mort_rate']