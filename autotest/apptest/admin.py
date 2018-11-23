from django.contrib import admin
from apptest.models import Appcase,Appcasestep

class AppcasestepAdmin(admin.TabularInline):
    list_display = ['appteststep','apptestobjname','appfindmethod','appevelement','appoptmethod','apptestdata','appassertdata','apptestresult','create_time','id','appcase']
    model = Appcasestep
    extra = 1

class AppcaseAdmin(admin.ModelAdmin):
    list_display = ['appcasename','apptestresult','apptester','id',]
    inlines = [AppcasestepAdmin]

admin.site.register(Appcase,AppcaseAdmin)