"""jiangye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings

from jiangyeapp import views
from django.conf.urls.static import static


from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #www.jiangye.com/index/  ->函数
    #注意，更新完路由信息后要重启django
    path('index/', views.index,name='index'),
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('tpl/',views.tpl),
    path('news/',views.news),
    path('something/',views.something),
    path('login/',views.login),
    path('orm/',views.orm),
    path('bootstrap5/',views.bootstrap5),
    #test
    path('info_list/',views.info_list),
    path('info/add/',views.info_add),
    path('info/delete/',views.info_delete),
    path('<year>/<int:month>/<slug:day>',views.myvariable,),
    path('index/',views.index,{'month':'2019/10/10'}),
    # path('test/',views.testjs),
    path('test/',views.youtube),
    path('test1/',views.test1),
    path('testjs/',views.testjs,name='testjs'),
    path('test2/',views.test1),

    

    
    
    

    # path('test/testjs/',views.testjs),
    #jaingyetest
    #path('book/',views.book),
    #path('book/detail<book_id>',views.book_detail),
 #movieslist
    
    path('moviesList/',include(('moviesList.urls','moviesList'),namespace='moviesList')),
    path('user/',include(('user.urls','user'),namespace='user')),#一定要加上app名字
    # 配置媒体文件的路由地址
    re_path('media/(?P<path>.*)',serve,
       {'document_root': settings.MEDIA_ROOT}, name='media'),
       #正则表达[0-9]从0到9，{4}四位
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',
views.mydate)   
    
   
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
