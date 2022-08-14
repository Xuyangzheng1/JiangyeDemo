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
from . import settings


from django.conf.urls.static import static


from django.views.static import serve

from jiangye.settings import MEDIA_ROOT
from django.contrib.auth.decorators import login_required
# from moviesForum import views 
from jiangyeapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #www.jiangye.com/index/  ->函数
    #注意，更新完路由信息后要重启django
    path('', views.index,name='index'),
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
    path('show_post_user/',views.show_post_user),
     path('showpostlist_pre',views.showpostlist_pre),
    path('showpost_list',views.showpost_list),
   
    path('info/add/',views.info_add),
    path('info/delete/',views.info_delete),
    path('<year>/<int:month>/<slug:day>',views.myvariable,),
    path('index/',views.index,{'month':'2019/10/10'}),
    # path('test/',views.testjs),
    path('test/',views.youtube),
    path('test1/',views.test1),
    path('testjs/',views.testjs,name='testjs'),
    # path(r'testjs/',as_views.testjs)
    # path(r'testjs/', login_required(views.testjs.as_view()), name='order'),
    # path('login/?next=/testjs/',views.testjs),

    path('test2/',views.test1),
    path('searchmovies/',views.testjs,name='searchmovies'),
    path('superindex/',views.superindex,name='superindex'),
    path('youtube/',views.youtube,name='youtube'),
    path('post/',views.publish_post,name='post'),
    path('show_post',views.show_post),
    path('quote/',views.Famous_Quotes),
    path('posts/<int:pk>/', views.detail, name='detail'),

    
    

    
    
    

    # path('test/testjs/',views.testjs),
    #jaingyetest
    #path('book/',views.book),
    #path('book/detail<book_id>',views.book_detail),
 #movieslist
    
    path('moviesList/',include(('moviesList.urls','moviesList'),namespace='moviesList')),
    path('user/',include(('user.urls','user'),namespace='user')),#一定要加上app名字
    path('moviesForum/',include(('moviesForum.urls','moviesForum'),namespace='moviesForum')),#一定要加上app名字

    
    # 配置媒体文件的路由地址
    re_path('media/(?P<path>.*)',serve,{'document_root': MEDIA_ROOT}, name='media'),
       #正则表达[0-9]从0到9，{4}四位
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',
views.mydate)   
    
   
    


]+static(settings.MEDIA_URL,document_root=MEDIA_ROOT)

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
