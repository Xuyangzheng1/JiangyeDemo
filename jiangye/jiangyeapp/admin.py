from django.contrib import admin

# Register your models here.
from moviesList import models

class moviesInfoAdmin(admin.ModelAdmin):
    list_display = ('movies_name','classification','release_data','movies_rating','movies_posts','img_url')


admin.site.register(models.moviesInfo,moviesInfoAdmin)


from . import models
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name','password','age','email')


admin.site.register(models.UserInfo,UserInfoAdmin)




from jiangyebook import models

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
