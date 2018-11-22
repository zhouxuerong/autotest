from django.contrib import admin
# from apitest.models import Apistep,Apitest,Apis
# from product.models import Product

# Register your models here.

# class ApistepAdmin(admin.TabularInline):
#     list_display = ('apiname','apiurl','apistep','apiparamvalue','api_method','apiresult','apistatus','create_time','id','apitest')  
#     '''还有一种比较特殊的情况，父子表的情况。编辑父表之后，再打开子表编辑，而且子表只能一条一条编辑，比较麻烦。
#         这种情况，我们也是可以处理的，将其放在同一个编辑界面中。
#        例如，有两个模型，一个是订单主表(BillMain)，记录主要信息；一个是订单明细(BillSub)，记录购买商品的品种和数量等。
#     '''
#     model = Apistep
#     extra = 1  
    
# @admin.register(Apitest)
# class ApitestAdmin(admin.ModelAdmin):
#     list_display = ('apitestname','apitestdesc','apitester','apitestresult','create_time','id')
#     inlines = [ApistepAdmin]
      


# class ApisAdmin(admin.ModelAdmin):
#     list_display=('apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id')  

# admin.site.register(Apis,ApisAdmin)


   
