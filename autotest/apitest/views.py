from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apitest.models import Apitest,Apistep,Apis
import pymysql

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
    return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list})

# @login_required
def apistep_manage(request):
    username = request.session.get('user','')
    apistep_list = Apistep.objects.all()
    return render(request,"apistep_manage.html",{"user":username,"apisteps":apistep_list})

def home(request):
    return render(request,"home.html")

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