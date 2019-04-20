from django.shortcuts import render
from MyTest import settings
from WebMonitor.models import *

# Create your views here.


def index(request):
    system_name = settings.SYSTEM_NAME
    host_info = Host_info.objects.order_by('app_name')

    if request.method == 'GET':
        return render(request, 'webmonitor/index.html', {'sys_name': system_name, 'host': host_info})
    else:
        return render(request, 'webmonitor/index.html', {'sys_name': system_name, 'host': host_info})


def list(request):
    return render(request, 'webmonitor/list.html', {})

