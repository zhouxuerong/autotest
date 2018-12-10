from django.shortcuts import render
from set.models import Set
from django.contrib.auth.models import User
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

def set_manage(request):
    username = request.session.get("user","")
    set_list = Set.objects.all()
    #生成paginator对象,定义每页显示10条记录
    paginator = Paginator(set_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        set_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        set_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        set_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
 
    return render(request,"set_manage.html",{"user":username,"sets":set_list})
    
def set_user(request):
    user_list = User.objects.all()
    username = request.session.get("user","")
    return render(request,"set_user.html",{"user":username,"users":user_list})

def setsearch(request):
    username = request.session.get("user","")
    search_setname = request.GET.get("setname","")
    set_list = Set.objects.filter(setname__icontains=search_setname)
    render(request,"set_manage.html",{"user":username,"sets":set_list})    