from django.contrib import admin

# Register your models here.
from moviesList import models



from user import models

# Register your models here.
#---------------------------------------
class MyadminSite(admin.AdminSite):
    site_header='giaogiao'
    site_title='giaogiao1'
#---------------------------------------
admin_site=MyadminSite(name='management')

class UserAdmin(admin.ModelAdmin):
    list_display =  ('phone','icon')
    #每页记录数
    list_per_page: 5
    #排序
    #ordering 

    #设置默认可编辑字段
    #list_editable=['phone']
    #过滤查询
    list_filter=['phone']
    #搜索查询
    search_fields= ['phone']
    #
   # date_hierarchy= 'date_joined'


admin.site.register(models.User,UserAdmin)
admin.site.site_header='亚洲动漫'
admin.site.site_title='亚洲动漫'

#xadmin
from django.contrib import admin

# Register your models here.
# from moviesList.models import Category, Page


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name',)}

# admin.site.register(Category, CategoryAdmin)

# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url')

# admin.site.register(Page, PageAdmin)
