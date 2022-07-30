from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings

from moviesList import views
#注意 urlpatterns有大写版本
urlpatterns = [

    path('',views.moviesLsit),
    path('luguan/',views.luguan),
    path('uploadfile/',views.uploadfile),
    path('showFile/',views.showFile),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('indext/',views.indext),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),#importment!!!!!
    path('add_category/', views.add_category, name='add_category'),       
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page')
    
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)