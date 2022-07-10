from django.urls import include, path


from . import views
#注意 urlpatterns有大写版本
urlpatterns = [

    path('',views.moviesLsit),
    path('luguan/',views.luguan),
    path('uploadfile/',views.uploadfile),
    path('showFile/',views.showFile),
    
    

]