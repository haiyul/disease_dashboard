from .models import *
from rest_framework import serializers
import django_filters


# 年龄分组的表
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


# 职业分组的表
class ProTbSerializer(serializers.ModelSerializer):
    month = serializers.CharField(source='month.month_cn')
    reg_name = serializers.CharField(source='reg_id.reg_name_crt')
    dis_name = serializers.CharField(source='dis_id.dis_name')

    class Meta:
        model = ProTb
        fields = ('year', 'month', 'reg_name', 'dis_name', 'pro_name',
                  'case_num', 'dea_num', 'inci_rate', 'mort_rate')


class ProTbFilterSet(django_filters.FilterSet):
    month = django_filters.CharFilter(field_name='month__month_cn')
    reg_name = django_filters.CharFilter(field_name='reg_id__reg_name_crt')
    dis_name = django_filters.CharFilter(field_name='dis_id__dis_name')

    class Meta:
        model = ProTb
        fields = ['year', 'month', 'reg_name', 'dis_name', 'pro_name',
                  'case_num', 'dea_num', 'inci_rate', 'mort_rate']


# 区域表
class RegTbSerializer(serializers.ModelSerializer):
    month = serializers.CharField(source='month.month_cn')
    reg_name = serializers.CharField(source='reg_id.reg_name_crt')
    dis_name = serializers.CharField(source='dis_id.dis_name')

    class Meta:
        model = RegTb
        fields = ('year', 'month', 'reg_name', 'dis_name',
                  'case_num', 'dea_num', 'inci_rate', 'mort_rate')


class RegTbFilterSet(django_filters.FilterSet):
    month = django_filters.CharFilter(field_name='month__month_cn')
    reg_name = django_filters.CharFilter(field_name='reg_id__reg_name_crt')
    dis_name = django_filters.CharFilter(field_name='dis_id__dis_name')

    class Meta:
        model = RegTb
        fields = ['year', 'month', 'reg_name', 'dis_name',
                  'case_num', 'dea_num', 'inci_rate', 'mort_rate']


from rest_framework_gis import serializers
from rest_framework.serializers import CharField, StringRelatedField


# geo全国地图api
class ProvinceBorderSerializer(serializers.GeoFeatureModelSerializer):
    reg_id = CharField(source='reg_id.reg_id')

    class Meta:
        model = ProvinceBorder
        geo_field = 'geom'
        auto_bbox = True
        # fields = ("id", 'name', 'py', 'geom', 'reg_id')
        fields = ("id", 'name', 'geom', 'reg_id', 'reg_id_set')


class ProvinceBorderFilterSet(django_filters.FilterSet):
    # Filter可以用外键，但是前面不能
    reg_id = django_filters.CharFilter(field_name='reg_id__reg_id')
    reg_id_not = django_filters.CharFilter(field_name='reg_id__reg_id', exclude=True)

    class Meta:
        model = ProvinceBorder
        fields = ["id", 'name', 'py', 'reg_id', 'reg_id_not']
