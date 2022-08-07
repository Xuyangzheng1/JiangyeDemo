from audioop import reverse

from email import message
from lib2to3.pgen2 import token
from os import path
import uuid
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from user.models import MySession


from user.models import userinformation

from django.conf import settings

from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth import authenticate, login as userlogin

from django.core.mail import send_mail

from django.contrib.sessions.backends.db import SessionStore

from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

from django.urls import reverse



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



#can not use session so use token_dict={}

global token_dict
token_dict={}
s=SessionStore()
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
        token = str(uuid.uuid4()).replace('-','')#随机数
        session= MySession.objects.create(token=token,Sessionkey=uuu.userid)
        session.save()

        print('[][][][][][][][][][][]>>>>>>',token)


        print('----------------------------------------------------------------------------------->regirest-token',token)
        token_dict={token:uuu.userid}
        # request.session[token]=uuu.userid
        print('giaogiaogaio-----------------------',token_dict)
        # print('----------------------------------------------------------------------------------->regirest-token',request.session)
        s=SessionStore()
        print('newSession---',token)
        s.create()
        s[token]=uuu.userid
        # print('----------------------------------------------------------------------------------->regirest-Session-token-value',s[token])
        request.session[token]={token:uuu.userid}
        # re=request.session[token]
        

        # print('-=-1-=1-=-1=-1=-1=-1', re)
        # s._set_session_key=token
        
        # print('----------------------------------------------------------------------------------->regirest-Session-token-keys',s.session_key)
        

        print('------=-=-=-=-=-=-=->>>>>',s[token])
        print('...................>>>>>>>>>>>>>>',token)
        print('------=-=-=-=-=-=-=->>>>>',s.session_key)
        
        path='http://127.0.0.1:8000/user/active?token={}'.format(token)
        subject='giaogiaogiao'

        message='''8====D >>>>>>>>>>
        <li>giao</li>
        <li><a href='{}'>点击激活</a>
        test:{}
        
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
        print('register------end--------------------------------------------------------------------------->',result)
        # #>------------------------------mail test-------------------------------------------{
       
        # return HttpResponse('注册成功')
        #}----------------------------test area-----------------------
        

        return redirect('http://localhost:8000/testjs/')
    return render(request, 'register.html')



def getSession(key):
    ll= MySession.objects.raw("select * from user_mysession where token='"+key+"'")
    if len(ll)==0:
        return ""
    return ll[0].Sessionkey
    
# def setSession(k,v):
#     mySession= MySession(k=k,value=v)
#     mySession.save()

def user_active(request):
    # MySession.objects.get(token=)
    
    token=request.GET.get('token')
    print('[][][][][][-----------------------][][][]][',token)
    uid=getSession(token)

    print('-=-=-=+-+_=_=_=',uid)

    

    user=userinformation.objects.get(pk=uid)
    user.is_active=1
    user.save()

    return redirect(reverse('user:login'))



    
    # print('.........................',ss[token])
    




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
            print('用户存在...')
            print(".....")
            if user.is_active:
                flag= check_password(pwd,user.password)
                print(flag)
                print('判断密码')
                if flag:
                    print('mimazhengque')
                    # return HttpResponse('success')
                    return redirect('http://127.0.0.1:8000/testjs/')
                    #zxy是傻逼
                else:
                    return render (request,'login.html',{'errmsg':'密码错误'})
                    
            else:    
                return render(request,'login.html',{'errmsg':'未激活'})
        
        else:
            return render(request,'login.html',{'errmsg':'密码错误giao'})
            

    print('11111')
    return render(request,'login.html')
    





















# ttt=request.session.get(token)
    # print(request.session.keys())
    # print('-=-=-=-=>>>ttt',ttt)
    # uid=request.session.get(token)
    # # request.session[token]
    # # print(request.session[token])
    # print('user_active_uid---------------------------------------------------------------------------------->',uid)

    # s=SessionStore(session_key=token)
    
    
    # print('165-----------------------------------------------------------',s.values())
    # # print('>>>>..。.。.。》》。。.。》》',s[token])
    


    # print(('user_activate---------------------s.Session_key------------------------------------------------------------>',s.session_key))
    # print('user_activate--------------------------------------------------------------------------------->',token)
    
    # # uid=token_dict.get('token')
    
    # ss=SessionStore(session_key=token)
    
    # print('----------------------------------------------------------------------------------->regirest-Session-token',ss.session_key)