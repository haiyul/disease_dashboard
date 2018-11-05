# from django.shortcuts import render
from rest_framework import viewsets, pagination
# from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *
from rest_framework_extensions.cache.mixins import CacheResponseMixin


class AggTbViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = AggTb.objects.all()
    serializer_class = AggTbSerializer
    # 取消最大页面数
    # pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filter_class = AggTbFilterSet


class ProTbViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = ProTb.objects.all()
    serializer_class = ProTbSerializer
    # 取消最大页面数
    # pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProTbFilterSet


class RegTbViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = RegTb.objects.all()
    serializer_class = RegTbSerializer
    # 取消最大页面数
    # pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filter_class = RegTbFilterSet


class ProvinceBorderViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = ProvinceBorder.objects.all()
    serializer_class = ProvinceBorderSerializer
    # 取消最大页面数
    # pagination_class = None
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProvinceBorderFilterSet
