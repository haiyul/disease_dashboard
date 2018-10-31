from django.conf.urls import url
from . import views

# from django.conf import settings
# from django.contrib.auth import  logout

app_name = 'home'
urlpatterns = [
    # url(r'^login/', views.login, name='login'),
    # url(r'^logout', views.login,  name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^home/', views.index, name='home')
]
