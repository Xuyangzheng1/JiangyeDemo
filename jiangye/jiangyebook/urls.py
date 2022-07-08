

from django.urls import path


from . import views
#注意 urlpatterns有大写版本
urlpatterns = [

    path('',views.book),
    path('detail/<book_id>',views.book_detail),
    path('test',views.test),

]