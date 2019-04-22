from django.shortcuts import render
from MyTest import settings
from WebMonitor.models import *
import os, time
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    system_name = settings.SYSTEM_NAME
    host_info = Host_info.objects.order_by('app_name')

    if request.method == 'GET' and 'app_id' in request.GET:
        aid = request.GET['app_id']
        # print(request.GET['app_id'])
        # print(request.GET['start_time'], type(request.GET['start_time']))
        host = Host_info.objects.filter(id=aid)[0]
        if not 'start_time' in request.GET or request.GET['start_time'] == ' ':
            start_time = int(str(time.time()).split('.')[0]) - 86400*3
            end_time = int(str(time.time()).split('.')[0])
            user_find = '0'
            # print("-------------")
            # TODO 绘图
        else:
            start_time = int(time.mktime(time.strptime(request.GET['start_time'], '%Y-%m-%d %H:%M:%S')))
            end_time = int(time.mktime(time.strptime(request.GET['end_time'], '%Y-%m-%d %H:%M:%S')))
            user_find = '1'
            # print("+++++++++++++")
            try:
                r = 5/0
                # TODO 绘图
            except Exception as e:
                info = ['系统提示：', '图型绘制失败,原因('+str(e)+')', '/WebMonitor/']
                return render(request, 'webmonitor/info.html', {'show_info': info})
        return render(request, 'webmonitor/index.html', {'sys_name': system_name, 'host': host_info})
    else:
        return render(request, 'webmonitor/index.html', {'sys_name': system_name, 'host': host_info})


def list(request):
    return render(request, 'webmonitor/list.html', {})


# def info(request):
#     return HttpResponseRedirect('/webmonitor/info/', {})

