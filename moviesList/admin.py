
from django.contrib import admin

from user.models import userinformation
from .models import moviesInformation


# Register your models here.
from moviesList.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)

@admin.register(moviesInformation)
class moviesInfo(admin.ModelAdmin):
     pass

@admin.register(userinformation)
class moviesInfo(admin.ModelAdmin):
     pass