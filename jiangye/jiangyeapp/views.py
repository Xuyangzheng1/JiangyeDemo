from asyncio.windows_events import NULL
from calendar import month
from contextlib import nullcontext
from email import message
from pickle import GET
from tkinter import image_types
from turtle import title
from unicodedata import name
from wsgiref.handlers import read_environ
from django.conf import settings
from django.forms import PasswordInput
from django.shortcuts import render, HttpResponse, redirect
from jiangyeapp.models import Department, UserInfo
from jiangyeapp import models
from django.core.mail import send_mail


# Create your views here.

def index(request,month):
    # return HttpResponse("welcome")
    #return render(request, "index.html",+month)错误写法
    return HttpResponse('路由之外的变量:'+month)


def user_list(request):
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    name = "giao哥"
    roles = ["xijingping", "江泽民", "曾宪国"]
    user_info = {"name": "giao", "salary": 12222, "roo": "crp"}
    data_list = [
        {"name": "giao1", "salary": 12422, "roo": "crp"},
        {"name": "giao2", "salary": 2, "roo": "cr23p"},
        {"name": "giao3", "salary": 92, "roo": "cr1p"},
        {"name": "giao4", "salary": 1202, "roo": "cr00p"},

    ]
    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info, "n4": data_list}, )


def news(request):
    return render(request, 'news.html')


def something(request):
    print(request.method)  # 获取请求方式

    print(request.GET)  # 在url上传送值 明面传输

    print(request.POST)  # 在请求体上提交数据 暗

    # return HttpResponse("fanhuineirong")
    return redirect("http://www.javdb.com")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # 如果是post请求就获取用户提交的数据

        # print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("password")
        if username == '1' and password == "1":
            # return HttpResponse("登陆成功")
            return redirect("http://www.javbus.com")
        else:
            # return HttpResponse("登陆成功")
            return render(request, "login.html", {"error_msg": "登陆失败"})


def orm(request):
    models.Department.objects.create(title="giao12")

    models.UserInfo.objects.create(name="曾宪国", age=12, size=21)
    models.UserInfo.objects.create(name="钱其德", age=1234, size=221)
    models.UserInfo.objects.create(name="高红梅", age=122, size=216)

    # UserInfo.objects.all().delete()
    # Department.objects.all().delete()
    UserInfo.objects.filter(id=111).delete()
    # data_list = UserInfo.objects.all()
    # -=-=-=--=-------------------------
    # for obj in data_list:
    #    print(obj.id,obj.name)
    # =======================
    # data_list = UserInfo.objects.filter(name="钱其德")
    # print(data_list)
    # ---------------------------------------------更新数据
    UserInfo.objects.filter(name="giaogiao").update(password="dsa")

    return HttpResponse("火花！一给窝里给gioagiao")


def info_list(request):
    # 获取数据库种所有用户信息
    datalist = UserInfo.objects.all()

    return render(request, "info_list.html", {"data_list": datalist})


def info_add(request):
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    if request.method == "GET":
        return render(request, "info_add.html")

    
    if user==NULL :
        # return render(request,"info_add.html",'3213')
            return HttpResponse('3213')
    else:
            UserInfo.objects.create(name=user, password=pwd, age=age)# 获取数据
            
   # except models.UserInfo.DoesNotExist:
       #return render(request,"info_add.html",'3213')
        
    

    return redirect("/info_list/")


def info_delete(request):
    nid = request.GET.get('nid')  # 提交方式是GET方式
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info_list/")

#test
# views.py的myvariable函数
from django.http import HttpResponse, JsonResponse

def myvariable(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))

def mydate(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))


def book(request):
    return HttpResponse('这是jiangyetest')

def book_detail(request,book_id):
    text = '图书id是 %s'% book_id
    return HttpResponse(text)

def register(request):
    if request.method == 'POST':
        username1 = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow=request.POST.get('allow')
        age=request.POST.get('age')
        date=request.POST.get('date')
        time1=request.POST.get('time')
        print(allow)
        #if allow !='on':
         #   return render(request,'register.html',{'errmsg':'huoyigeiwoligiaogiao'})
        uuu=UserInfo.objects.create(name=username1,password=pwd,email=email,age=age,date=date,create_time=time1)
    #userinfov.is_active()=0
        uuu.save()
        #发送邮件
        subject='youjian'
        message="huanying <br> <a href=''dianjijihuo" 
        #res=send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[email,])
        #print(res)

        return render(request,'tpl.html')
    return render(request,'register.html')


    
def check_user(request):
    username = request.GET.get('username')
    user=UserInfo.objects.filter(username=username).first
    

def login():
    return HttpResponse('login')
