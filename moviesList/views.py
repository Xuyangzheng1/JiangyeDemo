

from distutils import errors
import os
from plistlib import UID
from tkinter import image_names
from django import urls
from django.forms import ImageField
from django.http import HttpResponse
from django.shortcuts import redirect, render

from moviesList.forms import PageForm
from moviesList.forms import CategoryForm

from moviesList import models



from .models import Category, Page, moviesInformation
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
    queryset =models.moviesInformation.objects.all()

    user=moviesInformation.objects.filter()
    print('------------',user)
    
    #avatar_addr = user.get_avatar_url()

    #uurl= queryset.get_img_url_url()
        #img_url.debug('返回的图片链接是={}'.format(avatar_addr))

        #return successResultJson(data={"avatar": avatar_addr}, msg='修改成功')
    
    #image = request.FILES.get('imaurl/')
    #print(image,'------------------------------')
    
    return render(request,'movies_list.html',{'queryset':queryset})

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        #
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/moviesList/indext/')
        else:
            print(form.errors)    

    return render(request, 'add_category.html', {'form': form})        


def show_category(request, category_name_slug):
     
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None 
        context_dict['pages'] = None
    return render(request, 'category.html', context=context_dict)

def indext(request):
    return render(request,'indext.html')

    
def add_page(request, category_name_slug): 
    try:
        category = Category.objects.get(slug=category_name_slug) 
    except Category.DoesNotExist:
        category = None
    # You cannot add a page to a Category that does not exist...
    if category is None:
        return redirect('/add_category/')
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid(): 
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(urls.reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else: 
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'add_page.html', context=context_dict)  