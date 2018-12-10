from django.contrib import admin
from product.models import Product
from django.db import models
from apitest.models import Apis
from apptest.models import Appcase

class ApisAdmin(admin.TabularInline):
    list_display=('apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product') 
    model = Apis
    extra = 1

# Register your models here.
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('productname','productdesc','producter','create_time','id')
#     inlines = [ApisAdmin]
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productname','productdesc','create_time','id')
    inlines = [ApisAdmin]

class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcasename','apptestresult','create_time','id','product']
    model = Appcase 
    extra = 1



admin.site.register(Product) #把产品模块注册到Django admin后台并显示