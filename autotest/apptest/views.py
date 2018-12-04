from django.shortcuts import render
from apptest.models import Appcase,Appcasestep

def appcase_manage(request):
    appcase_list = Appcase.objects.all()
    username = request.session.get("user","")
    return render(request,"appcase_manage.html",{"user":username,"appcases":appcase_list})


def appcasestep_manage(request):
    appcasestep_list = Appcasestep.objects.all()
    username = request.session.get("user","")
    return render(request,"appcasestep_manage.html",{"user":username,"appcasesteps":appcasestep_list})  

def apptest_report(request):
    username = request.session.get("user","")
    return render(request,"apptest_report.html")

    
