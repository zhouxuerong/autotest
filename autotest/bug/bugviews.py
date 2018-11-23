from django.shortcuts import render
from bug.models import Bug
from django.contrib import auth

def bug_manage(request):
    username = request.session.get('user','')
    bug_list = Bug.objects.all()
    return render(request,"bug_manage.html",{'user':username,"bug_list":bug_list})

