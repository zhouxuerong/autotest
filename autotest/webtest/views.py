from django.shortcuts import render
from webtest.models import Webcase,Webcasestep

def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get("user","")
    return render(request,"webcase_manage.html",{"user":username,"webcases":webcase_list})


def webcasestep_manage(request):
    webcasestep_list = Webcasestep.objects.all()
    username = request.session.get("user","")
    return render(request,"webcasestep_manage.html",{"user":username,"webcasesteps":webcasestep_list})    