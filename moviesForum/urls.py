from django.contrib import admin
from django.urls import path

from moviesForum import views



urlpatterns = [

    path('index/', views.index, name="index"),  
    path('create/', views.create, name="create"),
   

    path('index/topic/<int:Blog_id>/', views.topic, name="topic"),    
    path('index/topic/<int:Blog_id>/reply/', views.reply, name="reply"),  
       
   
]