from django.shortcuts import render
import sys
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from apitest.models import Apitest,Apistep,Apis
import pymysql
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
# def test(request):
#     # return HttpResponse("hello test")
#     return render(request,"login.html")
def Login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home')
            return response
        else:
            return render(request,'login.html',{'error':"username or password error"})    
    return render(request,"login.html")      

# @login_required
def apitest_manage(request):
    username = request.session.get('user','')
    apitest_list = Apitest.objects.all()
    apitest_counts = Apitest.objects.all().count()
    paginator = Paginator(apitest_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        apitest_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        apitest_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        apitest_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
 
    return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list,"apitestcounts":apitest_counts})

# @login_required
def apistep_manage(request):
    username = request.session.get('user','')
    apitestid =request.GET.get("apitest.id",None)
    apitest = Apitest.objects.get(id=apitestid)
    apistep_list = Apistep.objects.all()
    return render(request,"apistep_manage.html",{"user":username,"apisteps":apistep_list,"apitest":apitest})

def apis_manage(request):
    username = request.session.get("user","")
    apis_list = Apis.objects.all()
    apis_counts = Apis.objects.all().count()
    paginator = Paginator(apis_list, 10)
    #从前端获取当前的页码数,默认为1
    page = request.GET.get('page',1)   
    #把当前的页码数转换成整数类型
    currentPage=int(page)
    try:
        print(page)
        apis_list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        apis_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        apis_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request,"apis_manage.html",{"user":username,"apiss":apis_list,"apiscounts":apis_counts})

# @login_required
def apisearch(request):
    username = request.session.get("user","")
    search_apitestname = request.GET.get("apitestname","")
    apitest_list=Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list})

def apissearch(request):
    username = request.session.get("user","")
    search_apisname = request.GET.get("apisname","")
    apis_list=Apis.objects.filter(apiname__icontains=search_apisname)
    return render(request,"apitest_manage.html",{"user":username,"apiss":apis_list})

def apistepsearch(request):
    username = request.session.get("user","")
    search_apistepname = request.GET.get("apistepname","")
    apistep_list=Apistep.objects.filter(apiname__icontains=search_apistepname)
    return render(request,"apitest_manage.html",{"user":username,"apisteps":apistep_list})

def home(request):
    return render(request,"home.html")

def welcome(request):
    return render(request,"welcome.html")

def left(request):
    return render(request,"left.html")


def logout(request):
    return render(request,"login.html")  

def test_report(request):
    username = request.session.get("user","")
    apis_list = Apis.objects.all()
    api_count = Apis.objects.all().count()
    db = pymysql.connect(user="root",db="autotest",passwd="password123",host="127.0.0.1")
    cursor = db.cursor()
    sql1 = "select count(id) from apitest_apis where apitest_apis.apistatus = 1"
    aa = cursor.execute(sql1) 
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    sql2 = "select count(id) from apitest_apis where apitest_apis.apistatus = 0"
    bb =   cursor.execute(sql2) 
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request,"report.html",{"user":username,"apis":apis_list,"apiscounts":api_count,"apis_pass_counts":apis_pass_count,"apis_fail_counts":apis_fail_count})