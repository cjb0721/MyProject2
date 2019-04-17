from django.conf.urls import url
from . import views


app_name = 'WebMonitor'


urlpatterns = [
    url(r'webindex/', views.index, name='index'),
    url(r'weblist/$', views.list, name='list'),
]