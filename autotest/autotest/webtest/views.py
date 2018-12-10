from django.shortcuts import render
from webtest.models import Webcase,Webcasestep
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    webcase_count = Webcase.objects.all().count()
    username = request.session.get("user","")
    paginator = Paginator(webcase_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        webcase_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        webcase_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        webcase_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
 
    return render(request,"webcase_manage.html",{"user":username,"webcases":webcase_list,"webcasecounts":webcase_count})


def webcasestep_manage(request):
    webcasestep_list = Webcasestep.objects.all()
    webcasestep_count = Webcasestep.objects.all().count()
    username = request.session.get("user","")
    paginator = Paginator(webcasestep_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        webcasestep_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        webcasestep_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        webcasestep_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
 
    return render(request,"webcasestep_manage.html",{"user":username,"webcasesteps":webcasestep_list,"webcasestepcounts":webcasestep_count})  

def websearch(request):
    username = request.session.get("user","")
    search_webcasename = request.GET.get("webcasename","")
    webcase_list=Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request,"webcase_manage.html",{"user":username,"webcases":webcase_list})

def webstepsearch(request):
    username = request.session.get("user","")
    search_webcasename = request.GET.get("webcasename","")
    webcasestep_list=Webcasestep.objects.filter(Webcasename__icontains=search_webcasename)
    return render(request,"webcasestep_manage.html",{"user":username,"webcasesteps":webcasestep_list})


