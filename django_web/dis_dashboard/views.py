from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *


class AggTbViewSet(viewsets.ModelViewSet):
    queryset = AggTb.objects.all()
    serializer_class = AggTbSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('year', 'month', 'reg_id', 'dis_id', 'agg_id', 'gd_id',
              'case_num', 'dea_num', 'inci_rate', 'mort_rate')
