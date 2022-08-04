from email import message
from lib2to3.pgen2 import token
from os import path
import uuid
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, JsonResponse


from user.models import userinformation

from django.conf import settings

from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth import authenticate, login as userlogin

from django.core.mail import send_mail



def book(request):
    return HttpResponse('这是jiangyetest')

def book_detail(request,book_id):
    text = '图书id是 %s'% book_id
    return HttpResponse(text)

def test(request):
    return HttpResponse('testjaingyebook')

def test730(request):
    name="giao"
    datetime=datetime.now()
    return render(request,'index')


def register(request):
    if request.method == 'POST':
        username1 = request.POST.get('user_name')
        pwd = request.POST.get('pwd')

        # cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        age = request.POST.get('age')
        # date = request.POST.get('date')
        time1 = request.POST.get('time')
        userimg = request.POST.get('userimg')
        print(allow)
        print(pwd)
        # if allow !='on':
        #   return render(request,'register.html',{'errmsg':'huoyigeiwoligiaogiao'})

        pwd = make_password(password=pwd)
        uuu = userinformation.objects.create(
            username=username1, password=pwd, email=email, age=age,create_time=time1,userImg=userimg)
    # userinformationv.is_active()=0
    #-----------------------------------------test area------------------------<>-----------
        uuu.is_active =0
        uuu.save()

        #>------------------------------mail test-------------------------------------------{
        # send_mail()
        token = str(uuid.uuid4()).replace('-','')
        token_dict={token:uuu.id}

        

        subject='giaogiaogiao'

        message='''8====D >>>>>>>>>>
        <li>giao</li>
        <li><a href='#'>点击激活</a>
        
        '''.format(path,path)
        print('>-------')
        print(email)
        print(settings.EMAIL_HOST_USER)
        
        result= send_mail(subject=subject,
                          message="",
                          from_email=settings.EMAIL_HOST_USER,
                          
                          recipient_list=[email],
                          html_message=message
                  )
        print(result)
        #>------------------------------mail test-------------------------------------------{
        # 
        # 
        # }
        return HttpResponse('注册成功')
        #}----------------------------test area-----------------------
        # 发送邮件
        
        # subject = 'youjian'
        # message = "huanying <br> <a href=''dianjijihuo"
        # res=send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[email,])
        # print(res)

        return redirect('http://localhost:8000/testjs/')
    return render(request, 'register.html')


def check_user(request):
   username= request.GET.get('username')
   user = userinformation.objects.filter(username=username).first()
   if user:
        return JsonResponse({'status':'fail','msg':'此用户名已被注册'})
   else:
        return JsonResponse({'status':'success','msg':'giao!'})


def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        pwd = request.POST.get('pwd')
        print(username)

        user = userinformation.objects.filter(username=username).first()
        
       
        if user:
            print('用户存在')
            if user.is_active:
                flag= check_password(pwd,user.password)
                print(flag)
                print('判断密码')
                if flag:
                    print('mimazhengque')
                    # return HttpResponse('success')
                    return render(request,'testjs.html')
                    
                else:
                    return render (request,'login.html',{'errmsg':'密码错误'})
                    
            else:    
                return render(request,'login.html',{'errmsg':'未激活'})
        
        else:
            return render(request,'login.html',{'errmsg':'密码错误giao'})
            

    print('11111')
    return render(request,'login.html')
    