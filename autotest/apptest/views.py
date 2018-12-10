from django.shortcuts import render
from apptest.models import Appcase,Appcasestep
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

def appcase_manage(request):
    appcase_list = Appcase.objects.all()
    appcase_count = Appcase.objects.all().count()
    username = request.session.get("user","")
    paginator = Paginator(appcase_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        appcase_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        appcase_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        appcase_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
 
    return render(request,"appcase_manage.html",{"user":username,"appcases":appcase_list,"appcasecounts":appcase_count})


def appcasestep_manage(request):
    appcasestep_list = Appcasestep.objects.all()
    appcasestep_count = Appcasestep.objects.all().count()
    username = request.session.get("user","")
    paginator = Paginator(appcasestep_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        appcasestep_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        appcasestep_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        appcasestep_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
 
    return render(request,"appcasestep_manage.html",{"user":username,"appcasesteps":appcasestep_list,"appcasestepcounts":appcasestep_count})  

def apptest_report(request):
    username = request.session.get("user","")
    return render(request,"apptest_report.html")

def appsearch(request):
    username = request.session.get("user","")
    search_appcasename = request.GET.get("appcasename","")
    appcase_list=Appcase.objects.filter(appcasename__icontains=search_appcasename)
    return render(request,"appcase_manage.html",{"user":username,"appcases":appcase_list})

def appstepsearch(request):
    username = request.session.get("user","")
    search_appcasename = request.GET.get("appcasename","")
    appcasestep_list=Appcasestep.objects.filter(appcasename__icontains=search_appcasename)
    return render(request,"appcasestep_manage.html",{"user":username,"appcasesteps":appcasestep_list})


    
