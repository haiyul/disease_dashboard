from django.shortcuts import render
from rest_framework import viewsets, pagination
# from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *
from rest_framework_extensions.cache.mixins import CacheResponseMixin


class AggTbViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = AggTb.objects.all()
    serializer_class = AggTbSerializer
    pagination_class = None  # 区划信息不分页
    filter_backends = (DjangoFilterBackend,)
    filter_class = AggTbFilterSet
