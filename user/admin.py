from django.contrib import admin
from user.models import MySession



class MySessionAdmin(admin.ModelAdmin):
    list_display=('token','Sessionkey')

    
admin.site.register(MySession,MySessionAdmin)