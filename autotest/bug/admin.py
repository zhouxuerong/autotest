from django.contrib import admin
from bug.models import Bug

class BugAdmin(admin.ModelAdmin):
    list_dispaly = ['bugname','bugdetail','bugstatus','bug_level','bugcreater','bugassign','create_time','id']

admin.site.register(Bug)    

