from django.contrib import admin
from .models import *
# Register your models here.


class Host_info_Admin(admin.ModelAdmin):
    list_filter = ['app_name', 'idc']
    search_fields = ['app_name', ]
    list_per_page = 10


admin.site.register(Host_info, Host_info_Admin)


class Monitor_data_Admin(admin.ModelAdmin):
    list_filter = ['fid', 'datetime']
    list_per_page = 10


admin.site.register(Monitor_data, Monitor_data_Admin)

