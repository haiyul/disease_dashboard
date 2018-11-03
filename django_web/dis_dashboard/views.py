from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class AggTbViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AggTb.objects.all().order_by('id')
    serializer_class = AggTbSerializer
