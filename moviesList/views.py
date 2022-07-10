

import os
from plistlib import UID
from tkinter import image_names
from django import urls
from django.forms import ImageField
from django.http import HttpResponse
from django.shortcuts import render
from moviesList import models



from .models import moviesInfo
from moviesList import models

# Create your views here.

def moviesLsit(request):
    
    return render(request,"movies_list.html")


def luguan(request):
    html = '<h1>lugaun'
    return HttpResponse(html)

def uploadfile(request):
    print(request)
    return('tupain')

def showFile(request):
    #moviesInfo.objects.filter(movies_name='ipx-678')#数据库对应的名字
    queryset =models.moviesInfo.objects.all()

    user=moviesInfo.objects.filter()
    print('------------',user)
    
    #avatar_addr = user.get_avatar_url()

    #uurl= queryset.get_img_url_url()
        #img_url.debug('返回的图片链接是={}'.format(avatar_addr))

        #return successResultJson(data={"avatar": avatar_addr}, msg='修改成功')
    
    #image = request.FILES.get('imaurl/')
    #print(image,'------------------------------')
    
    return render(request,'movies_list.html',{'queryset':queryset})


