from django.shortcuts import render

# Create your views here.


def index(request):
    # if request.method == 'GET':
    return render(request, 'webmonitor/index.html', {'username':'ggb'})


def list(request):
    return render(request, 'webmonitor/list.html', {})

