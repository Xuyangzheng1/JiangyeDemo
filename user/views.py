from audioop import reverse

from email import message
from lib2to3.pgen2 import token
from os import path
import uuid
from django.shortcuts import redirect, render

from django.contrib.auth import login

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.db import connection
from moviesForum.models import Reply
from moviesList.models import BlogPost
from user.models import MySession, WatchMovie
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from user.models import userinformation as User

from django.conf import settings

from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth import authenticate, login as userlogin,logout

from django.core.mail import send_mail

from django.contrib.sessions.backends.db import SessionStore

from importlib import import_module
from django.conf import settings
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

from django.urls import reverse



def book(request):
    return HttpResponse('这是jiangyetest')

def book_detail(request,book_id):
    book_id=90
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
def userimg_upload(req):
    file = req.FILES.get('file', None)        
    path = default_storage.save('C:\\Users\\Administrator\\workspace\\jiangyenew\\JiangyeDemo\\media\\usersImg/' + file.name, ContentFile(file.read()))
    re={}
    re['']=0
    return JsonResponse(re)
    
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
        # print("path------------",path)
        print(allow)
        print(pwd)
     

        # pwd = make_password(password=pwd)
        uuu = User.objects.create_user(
            username=username1, password=pwd, email=email, age=age,create_time=time1,userImg=userimg)
    # userinformationv.is_active()=0
    #-----------------------------------------test area------------------------<>-----------
        uuu.is_active =1
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

    

    user=User.objects.get(pk=uid)
    user.is_active=1
    user.save()

    return redirect(reverse('user:login'))



    
  
    




def check_user(request):
   username= request.GET.get('username')
   user = User.objects.filter(username=username).first()
   if user:
        return JsonResponse({'status':'fail','msg':'此用户名已被注册'})
   else:
        return JsonResponse({'status':'success','msg':'giao!'})


from django.contrib.auth.backends import ModelBackend
from django.contrib import auth

# from django.contrib.auth.models import User   
# class userloginMobileBackend(ModelBackend):
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        pwd = request.POST.get('pwd')
        print(username)

        user = User.objects.filter(username=username).first()
        
    
        if user:
            print('用户存在...')
            print(".....")
            if user.is_active:
                # flag= check_password(pwd,user.password)
                
                flag = authenticate(username=username, password=pwd)
                print(flag)
                print('判断密码')
                if flag:
                    print('mimazhengque')
                    # return HttpResponse('success')
                    login(request,flag,backend='django.contrib.auth.backends.ModelBackend')
                    print('////////////////userobj',login(request,flag))
                    if request.user.is_authenticated:
                        print('登录')
                        print(request.user.is_authenticated)


                       
                    else:
                        print('未登录')    
                        print(request.user.is_authenticated)


                    
                    return redirect('/moviesForum/index/')
                    #zxy是傻逼
                else:
                    return render (request,'login.html',{'errmsg':'密码错误'})
                    
            else:    
                return render(request,'login.html',{'errmsg':'未激活'})
        
        else:
            return render(request,'login.html',{'errmsg':'密码错误giao'})
            

    print('11111')
    return render(request,'login.html')
    




def loginoutUser(request):
    logout(request)

    return redirect('/index/')




def base(request):
    return render(request,'tbase.html')

from django.http import Http404
def user(request, user_name):
    """ 用户 GET """
    users = list(User.objects.filter(username=user_name))
    if len(users) == 0:
        raise Http404("用户不存在")
    user_obj = users[0]
    if request.user:
        return render(request, 'useraccount.html', {
            'user': user_obj,
            'topics': BlogPost.objects.filter(user_id=user_obj),
            'replies': Reply.objects.filter(reply_user=user_obj),
            'logged_in_user': request.user
        })
    else:
        return render(request, 'useraccount.html', {
            'user': user_obj,
            'topics': BlogPost.objects.filter(user_id=user_obj),
            'replies': Reply.objects.filter(reply_user=user_obj),
        })
def watchList(request, user_name):
    """ 用户 GET """
    users = list(User.objects.filter(username=user_name))
    if len(users) == 0:
        raise Http404("用户不存在")
    user_obj = users[0]
    ll=WatchMovie.objects.raw("select m.id,m.movies_title as movieName,m.movie_imdblink as url1,m.movie_natflixlink as url2,m.img_url as img from movieslist_moviesinformation_user_id u left join  movieslist_moviesinformation m on m.id=moviesinformation_id where u.userinformation_id='"+str(user_obj.userid)+"'")
    return render(request, 'watch_list.html', {
        'user': user_obj,
        'movies': ll,
        'logged_in_user': request.user
    })
    
def add2watchlist(req):
    userId=req.POST.get("userId")
    movieId=req.POST.get("movieId")
    cur = connection.cursor()
    re={}
    
    ll=WatchMovie.objects.raw("select m.id,m.movies_title as movieName,m.movie_imdblink as url1,m.movie_natflixlink as url2,m.img_url as img from movieslist_moviesinformation_user_id u left join  movieslist_moviesinformation m on m.id=moviesinformation_id where m.id='"+movieId+"' and u.userinformation_id='"+userId+"'")
    if len(ll)>0:
        re['code']=500
        return JsonResponse(re)
    re['code']=200  
    cur.execute("insert into movieslist_moviesinformation_user_id(moviesinformation_id,userinformation_id) value('"+movieId+"','"+userId+"')")
    
    
    return JsonResponse(re)
