

from unicodedata import name
from django.urls import path,re_path

from django.conf.urls.static import static
from django.conf import settings
from user import views

from django.views.static import serve
from django.contrib.auth import views as auth_views
#注意 urlpatterns有大写版本

app_name ='user'

urlpatterns = [

    path('',views.book),
    path('detail/<book_id>',views.book_detail),
    path('test',views.test),
    path('userimg_upload',views.userimg_upload),
    path('register/',views.register,name='register'),
    path('check_user/',views.check_user,name='check_user'),
    path('login/',views.userlogin,name='login'),

    path('tbase/',views.base),

    
    path('active/',views.user_active,name='active'),
    path('logout/',views.loginoutUser,name='logout'),
    re_path('media/(?P<path>.*)',serve,{'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path('media/usersImg/(?P<path>.*)',serve,{'document_root': settings.MEDIA_ROOT}, name='media'),
    


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)