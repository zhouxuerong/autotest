from django.shortcuts import render
from bug.models import Bug
from django.contrib import auth
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def bug_manage(request):
    username = request.session.get('user','')
    bug_list = Bug.objects.all()
    bug_count = Bug.objects.all().count()
    paginator = Paginator(bug_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        bug_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        bug_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        bug_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
 
    return render(request,"bug_manage.html",{'user':username,"bug_list":bug_list,"bugcounts":bug_count})

def bugsearch(request):
    username = request.session.get("user","")
    search_bugname = request.GET.get("bugname","")
    bug_list = Bug.objects.filter(bug__icontains=search_bugname)
    render(request,"product_manage.html",{"user":username,"bugs":bug_list}) 
