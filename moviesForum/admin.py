from django.contrib import admin

# Register your models here.
from .models import Reply

class ReplyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Reply,ReplyAdmin)