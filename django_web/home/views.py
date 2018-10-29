from django.shortcuts import render, redirect
# from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, 'home/index.html')

