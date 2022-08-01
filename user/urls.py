

from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from . import views
#注意 urlpatterns有大写版本
urlpatterns = [

    path('',views.book),
    path('detail/<book_id>',views.book_detail),
    path('test',views.test),
    path('register/',views.register,name='register'),
    path('check_user/',views.check_user,name='check_user')
    


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)