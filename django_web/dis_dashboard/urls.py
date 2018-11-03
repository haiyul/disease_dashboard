from django.conf.urls import url, include
from rest_framework import routers
from dis_dashboard import views

router = routers.DefaultRouter()
router.register(r'AggTb', views.AggTbViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-AggTb/', include('rest_framework.urls', namespace='rest_framework'))
]