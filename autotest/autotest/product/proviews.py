from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def product_manage(request):
    username = request.session.get("user",'')
    product_list = Product.objects.all()
        #生成paginator对象,定义每页显示10条记录
    paginator = Paginator(product_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        product_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        product_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request,"product_manage.html",{"user":username,"products":product_list})

def productsearch(request):
    username = request.session.get("user","")
    search_productname = request.GET.get("productname","")
    product_list = Product.objects.filter(productname__icontains=search_productname)
    render(request,"product_manage.html",{"user":username,"products":product_list}) 