from ast import Param
import json
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
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
from isodate import parse_duration
# pip install pipenv
# pipenv install isodate
# pip install -U rdflib
import requests
from django.conf import settings
import imdb



# Create your views here.


def index(request):
    # return HttpResponse("welcome")
    # return render(request, "index.html",+month)错误写法
    return render(request, 'index.html')


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

    if user == NULL:
        # return render(request,"info_add.html",'3213')
            return HttpResponse('3213')
    else:
            UserInfo.objects.create(name=user, password=pwd, age=age)  # 获取数据

   # except models.UserInfo.DoesNotExist:
       # return render(request,"info_add.html",'3213')

    return redirect("/info_list/")


def info_delete(request):
    nid = request.GET.get('nid')  # 提交方式是GET方式
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info_list/")


# test
# views.py的myvariable函数


def myvariable(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))


def mydate(request, year, month, day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))


def book(request):
    return HttpResponse('这是jiangyetest')


def book_detail(request, book_id):
    text = '图书id是 %s' % book_id
    return HttpResponse(text)


def register(request):
    if request.method == 'POST':
        username1 = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        age = request.POST.get('age')
        date = request.POST.get('date')
        time1 = request.POST.get('time')
        print(allow)
        # if allow !='on':
         #   return render(request,'register.html',{'errmsg':'huoyigeiwoligiaogiao'})
        uuu = UserInfo.objects.create(
            name=username1, password=pwd, email=email, age=age, date=date, create_time=time1)
    # userinfov.is_active()=0
        uuu.save()
        # 发送邮件
        subject = 'youjian'
        message = "huanying <br> <a href=''dianjijihuo"
        # res=send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[email,])
        # print(res)

        return render(request, 'tpl.html')
    return render(request, 'register.html')


def check_user(request):
    username = request.GET.get('username')
    user = UserInfo.objects.filter(username=username).first


def login():
    return HttpResponse('login')


def bootstrap5(request):
    return render(request, 'bootstrap5.html')


def youtube(request):
    url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    # if request.method == "GET":
    #

    #     print(search_params['q'])
    #     return render(request,'test.html',context)
    search_params = {
        'part': 'snippet',
        'q': '1',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 10,
        'type': 'video',

    }
    search_params['q'] = request.POST.get('search')

    # print("==========",search_params['q'],"=========================================================================================================================================================================================")

    r = requests.get(url, params=search_params)

    # print(r.text)
    # print(r.json()['items'][0]['id']['videoId'])
    video_ids = []
    resultes = r.json()['items']
    for result in resultes:
       # print(result['id']['videoId'])
        video_ids.append(result['id']['videoId'])

    video_params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet,contentDetails',
        'id': ','.join(video_ids),
        'maxResults': 200,

    }  # 二次搜索

    r = requests.get(video_url, params=video_params)
    resultes = r.json()['items']
    # print(r.text)
    print(resultes)
    videos = []
    for result in resultes:

        video_data = {
            'title': result['snippet']['title'],
            'id': result['id'],
            'url': f'https://www.youtube.com/watch?v={ result["id"] }',
            # 持续时间
            'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds()//60),
            'thumbnail': result['snippet']['thumbnails']['high']['url'],  # 略缩图
        }
        print(video_data)
        videos.append(video_data)
    # print(videos)
    context = {
        'videos': videos
    }
    print(context)
    return render(request, 'test.html', context)

     # print(result)
        # print(result['snippet']['title'])
        # print(result['id'])
        # print(parse_duration(result['contentDetails']['duration']).total_seconds()//60)#秒
        # print(result['snippet']['thumbnails']['high']['url'])
         # print(result['kind'])
       # print(result['snippet']['channelId'])

    
def test1(request):


#https://rapidapi.com/apidojo/api/online-movie-database/

    url = "https://online-movie-database.p.rapidapi.com/auto-complete"

    querystring = {
                    "q":"Avengers"#Avengers
}
#-----------------------------------------------------------------
    
    headers = {
	"X-RapidAPI-Key": "300c876097msha9c4cc55679cfb6p1fe8ccjsn430c7177ad1b",
	"X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
}

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    fielddict = response.json()

    
    moviesdata = []
    for x in range(0,len(fielddict)):
        print('-----------------------------------------')
        # print(fielddict.get('d')[x]['i']['height'])
        print(fielddict.get('d')[x]['i']['imageUrl'])
        # print(fielddict.get('d')[x]['i']['width'])
        print(fielddict.get('d')[x]["id"])
        print(fielddict.get('d')[x]["l"])#The Avengers
        print(fielddict.get('d')[x]["q"])#feature
        print(fielddict.get('d')[x]["s"])#Robert Downey Jr., Chris Evans
        print(fielddict.get('d')[x]["rank"]) #评分


        moviesInfo = {
            'imageUrl':fielddict.get('d')[x]['i']['imageUrl'],
            #https://www.imdb.com/title/tt10240638/
            'movieId':f'''https://www.imdb.com/title/{ fielddict.get('d')[x]["id"] }''',
            
            'movieName':fielddict.get('d')[x]["l"],
            'movieType':fielddict.get('d')[x]["q"],
            'movieActor':fielddict.get('d')[x]["s"],
            'movieRank':fielddict.get('d')[x]["rank"],

        }

        moviesdata.append(moviesInfo)    
    context = {
        'moviesdata': moviesdata
    }
    return render(request,'test1.html',context)



#ajax
def testjs(request):
    if request.method == 'POST':
        n1=str(request.POST.get('n1'))
        n2=str(request.POST.get('n2'))
    
        print('n1'+n1)
        print('------')
        print('n2'+n2)
        return HttpResponse(n1+n2)
   
    
    return render(request,"testjs.html")

    
   # return HttpResponse('adsdasdasdasdasd')



























































































        #  video_data = {
        #     'title': result['snippet']['title'],
        #     'id': result['id'],
        #     'url': f'https://www.youtube.com/watch?v={ result["id"] }',
        #     # 持续时间
        #     'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds()//60),
        #     'thumbnail': result['snippet']['thumbnails']['high']['url'],  # 略缩图
        # }



        # print('>------------------------------i')
        # # print(fielddict.get('d')[x]['i'])#{'height': 2048, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg', 'width': 1382}

        # print(fielddict.get('d')[x]['i']['height'])
        # print(fielddict.get('d')[x]['i']['imageUrl'])
        # print(fielddict.get('d')[x]['i']['width'])
        # print('>------------------------------i')



        # print(fielddict.get('d')[x]['id'])#tt4154796
        # print(fielddict.get('d')[x]['l'])#Avengers: Endgame
        # print(fielddict.get('d')[x]['q'])#feature
        # print(fielddict.get('d')[x]['rank'])#157
        # print(fielddict.get('d')[x]['s'])#Robert Downey Jr., Chris Evans
        # print('>-----------------------11-------i')
        # print(fielddict.get('d')[0]['v'][x]["i"])
        # print('>----------------------11--------i')   

#============================================================================================================================================================================================================
        # print(fielddict.get('d')[0]['i'])#{'height': 2048, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg', 'width': 1382}
        # print(fielddict.get('d')[0]['id'])#tt4154796
        # print(fielddict.get('d')[0]['l'])#Avengers: Endgame
        # print(fielddict.get('d')[0]['q'])#feature
        # print(fielddict.get('d')[0]['rank'])#157
        # print(fielddict.get('d')[0]['s'])#Robert Downey Jr., Chris Evans


        # print(fielddict.get('d')[0]['v'][x]["i"]['height'])#1080
        # print(fielddict.get('d')[0]['v'][x]["i"]['imageUrl'])#https://m.media-amazon.com/images/M/MV5BOThlNjdhZmQtNzlkOS00M2VjLWI0ZjUtZDExZDI1MjRhZGFkXkEyXkFqcGdeQW1yb3NzZXI@._V1_.jpg
        # print(fielddict.get('d')[0]['v'][x]['i']['width'])#1920

        # print(fielddict.get('d')[0]['v'][x]['id'])#vi2163260441
        # print(fielddict.get('d')[0]['v'][x]['l'])#"Policy" Trailer
        # print(fielddict.get('d')[0]['v'][x]['s'])#1:06
        # print(fielddict.get('d')[0]['vt'])#117
        # print(fielddict.get('d')[0]['y'])#2019
#i:




       

    
    




# v:电影截图

{"d":[{"i":{"height":2048,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg",
    "width":1382},
"id":"tt4154796",
"l":"Avengers: Endgame",
"q":"feature",
"rank":157,
"s":"Robert Downey Jr., Chris Evans",

"v":[{"i":{"height":1080,"imageUrl":"https://m.media-amazon.com/images/M/MV5BOThlNjdhZmQtNzlkOS00M2VjLWI0ZjUtZDExZDI1MjRhZGFkXkEyXkFqcGdeQW1yb3NzZXI@._V1_.jpg",
"width":1920},
"id":"vi2163260441",
"l":"\"Policy\" Trailer",
"s":"1:06"},
{"i":{"height":1080,"imageUrl":"https://m.media-amazon.com/images/M/MV5BZTFiN2Y4NzEtNDBiNC00MGRiLWFjODAtMzFiYTY2NmE5YmZhXkEyXkFqcGdeQWplZmZscA@@._V1_.jpg",
"width":1920},
"id":"vi2232337177",
"l":"The 6 Most Romantic Moments in the Marvel Cinematic Universe",
"s":"1:48"},

{"i":{"height":1080,"imageUrl":"https://m.media-amazon.com/images/M/MV5BZTNhMWM0M2ItMDY1Ny00MmQ5LWI3N2QtYmY4Njc2MWEyMTYzXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg",
"width":1920},
"id":"vi1865596185",
"l":"\"Stakes\" Featurette",
"s":"1:01"}],
"vt":117,
"y":2019},#<--先写到这


{"i":{"height":2048,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_.jpg",
"width":1382},
"id":"tt4154756",
"l":"Avengers: Infinity War",
"q":"feature",
"rank":267,"s":"Robert Downey Jr., Chris Hemsworth",
"v":[{"i":{"height":733,
"imageUrl":"https://m.media-amazon.com/images/M/MV5BYjJiZTcxYzEtODFlZi00M2UzLTg5NTgtYWMxMGNkMWJiNmRjXkEyXkFqcGdeQXBrZWVzZXk@._V1_.jpg",
"width":1777},
"id":"vi528070681",
"l":"Chant TV Spot",
"s":"1:01"},
{"i":{"height":1080,
"imageUrl":"https://m.media-amazon.com/images/M/MV5BZTFiN2Y4NzEtNDBiNC00MGRiLWFjODAtMzFiYTY2NmE5YmZhXkEyXkFqcGdeQWplZmZscA@@._V1_.jpg",
"width":1920},
"id":"vi2232337177",
"l":"The 6 Most Romantic Moments in the Marvel Cinematic Universe",
"s":"1:48"},
{"i":{"height":1080,
"imageUrl":"https://m.media-amazon.com/images/M/MV5BMTFkNmVhYjYtZTVjYS00YzUxLWEwNDAtM2MzYjIxOWYwMGQyXkEyXkFqcGdeQXRodW1ibmFpbC1pbml0aWFsaXplcg@@._V1_.jpg",
"width":1920},
"id":"vi3110647833",
"l":"The 10-Year Legacy of the Marvel Cinematic Universe",
"s":"4:36"}],
"vt":95,
"y":2018},

{"i":{"height":1184,"imageUrl":"https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
"width":800},
"id":"tt0848228",
"l":"The Avengers",
"q":"feature",
"rank":511,"s":"Robert Downey Jr., Chris Evans","y":2012},

{"i":{"height":1280,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_.jpg",
"width":864},
"id":"tt2395427",
"l":"Avengers: Age of Ultron",
"q":"feature",
"rank":856,
"s":"Robert Downey Jr., Chris Evans",
"y":2015},

{"i":{"height":582,
"imageUrl":"https://m.media-amazon.com/images/M/MV5BZWQwZTdjMDUtNTY1YS00MDI0LWFkNjYtZDA4MDdmZjdlMDRlXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg",
"width":427},"id":"tt0054518",
"l":"The Avengers","q":"TV series","rank":4354,"s":"Patrick Macnee, Diana Rigg",
"y":1961,
"yr":"1961-1969"},

{"i":{"height":2048,"imageUrl":"https://m.media-amazon.com/images/M/MV5BMTY0NTUyMDQwOV5BMl5BanBnXkFtZTgwNjAwMTA0MDE@._V1_.jpg",
"width":1526},
"id":"tt2455546",
"l":"Avengers Assemble",
"q":"TV series",
"rank":9693,
"s":"Roger Craig Smith, Troy Baker",
"y":2012,"yr":"2012-2019"},

{"i":{"height":742,
"imageUrl":"https://m.media-amazon.com/images/M/MV5BYWE1NTdjOWQtYTQ2Ny00Nzc5LWExYzMtNmRlOThmOTE2N2I4XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg",
"width":493},
"id":"tt0118661",
"l":"The Avengers",
"q":"feature",
"rank":9853,
"s":"Ralph Fiennes, Uma Thurman",
"y":1998},

{"i":{"height":1176,
"imageUrl":"https://m.media-amazon.com/images/M/MV5BYzA4ZjVhYzctZmI0NC00ZmIxLWFmYTgtOGIxMDYxODhmMGQ2XkEyXkFqcGdeQXVyNjExODE1MDc@._V1_.jpg",
"width":800},
"id":"tt1626038",
"l":"The Aveng Avengers: Earth's Mightiest Heroes",
"q":"TV series",
"rank":10340,
"s":"Eric Loomis, Colleen O'Shaughnessey",
"y":2010,"yr":"2010-2012"}],
"q":"avengers",
"v":1}




#-------------------------------------commit--------------------------
    # print(fielddict.get('d')[0]['v'][0]['i']['imageUrl'])
    # print(fielddict.get('d')[0]['v'][0]['i']['width'])
    # print(fielddict.get('d')[0]['v'][0]['i']['id'])
    # print(fielddict.get('d')[0]['v'][0]['i']['l'])
    # print(fielddict.get('d')[0]['v'][0]['i']['s'])

    # print(fielddict.get('d')[0]['i'])
    # print(fielddict.get('d')[0]['i'])

#     # print(fielddict.get('Search')[0]['Year'])
#     # print(fielddict.get('Search')[0]['imdbID'])
#     # print(fielddict.get('Search')[0]['Poster'])
#-------------------------------------commit--------------------------



























   #https://rapidapi.com/rapidapi/api/movie-database-alternative/

#     url = "https://movie-database-alternative.p.rapidapi.com/"

#     querystring = {"s":"Avengers Endgame",
#                    "r":"json",
#                 "page":"1"}

#     headers = {
# 	"X-RapidAPI-Key": "300c876097msha9c4cc55679cfb6p1fe8ccjsn430c7177ad1b",
# 	"X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
# }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     # print(response.text)
#     fielddict = response.json()
#     # for fie in fielddict:
#     #     # print('fie:'+ fie)#键
#     #     # print('============================================')
#     #     # print(fielddict[fie])#值
#     #     # #打印Search列表
#     #     # print('>---------------------------------------------')
#     #     # print(fielddict['Search'][0])
#     #     # print(fielddict['Search'][1])
#     #     # print(fielddict['Search'][2])
#     #     # print('>---------------------------------------------')
#         #打印列表中的字典
#     #     {"Search":[{"Title":"Avengers: Endgame",
#     #              "Year":"2019",
#     #            "":"tt4154796",
#     #              "Type":"movie",
#     #            "Poster":"https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg"},

#     #            {"Title":"Avengers: Endgame and the Latest Captain Marvel Outrage!!",
#     #              "Year":"2019",
#     #            "imdbID":"tt10025738",
#     #              "Type":"movie",
#     #            "Poster":"https://m.media-amazon.com/images/M/MV5BZjg2ZTM3OTgtY2ExMS00OGM4LTg3NDEtNjQ0MjJiZDFmMGFkXkEyXkFqcGdeQXVyMDY3OTcyOQ@@._V1_SX300.jpg"},

#     #            {"Title":"Marvel Studios' Avengers: Endgame LIVE Red Carpet World Premiere",
#     #              "Year":"2019",
#     #            "imdbID":"tt10240638",
#     #              "Type":"movie",
#     #            "Poster":"https://m.media-amazon.com/images/M/MV5BNThjZDgwZTYtMjdmYy00ZmUyLTk4NTUtMzdjZmExODQ3ZmY4XkEyXkFqcGdeQXVyMjkzMDgyNTg@._V1_SX300.jpg"},

#     #            {"Title":"Avengers Endgame: the Butt Plan",
#     #              "Year":"2019",
#     #            "imdbID":"tt10399328",
#     #              "Type":"movie",
#     #            "Poster":"https://m.media-amazon.com/images/M/MV5BNTQ1OWQzODktMTY3Zi00OTQxLWExOTYtZTNjZjY5ZTY4M2UyXkEyXkFqcGdeQXVyMTAzMzk0NjAy._V1_SX300.jpg"},

#     #            {"Title":"Avengers: Endgame (2019)",
#     #              "Year":"2019",
#     #            "imdbID":"tt16416424",
#     #              "Type":"movie",
#     #            "Poster":"N/A"},
#     #            {"Title":"Avengers: Endgame (2019) - Spoiler Full Review",
#     #              "Year":"2019",
#     #            "imdbID":"tt17978032",
#     #              "Type":"movie",
#     #            "Poster":"N/A"}],
#     # "totalResults":"6",
#     # "Response":"True"}
#     # test1 = fielddict['Search'][len(fielddict)]

#     # for w in test1:
#     #     o=test1.get(w)
#     #     print(">-"+o)

#     # text=fielddict['Search'][0]
#     # for i in text:
#     #     print("text:"+i)
#     #-------------------------------------------------------
    
#     print('<--='.join(fielddict))
#     fielddict.get('Search')
#     # print(fielddict.get('Search')[0]['Title'])
#     # print(fielddict.get('Search')[0]['Year'])
#     # print(fielddict.get('Search')[0]['imdbID'])
#     # print(fielddict.get('Search')[0]['Poster'])


#     # print(fielddict.get('Search')[1])
#     # print(fielddict.get('Search')[2])
#     # print(fielddict.get('Search')[3])
#     for i in range(0,len(fielddict)):
#           print(fielddict.get('Search')[i]['Title'])
#           print(fielddict.get('Search')[i]['Year'])
#           print(fielddict.get('Search')[i]['imdbID'])
#           print(fielddict.get('Search')[i]['Poster'])

        

   
    

   
    

    # {'IMDBmoviesInfo': ['Avengers: Endgame',
    #      '2019', 
    #     'movie',
    #  'tt4154796',
    #  'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg']}



 # text.get('Title')
    # text.get('Title')
    # text.get('Title')
    # print('>-------->====')
    # print(text.get('Title'))
    # print(text.get('Year'))
    # print(text.get('Type'))
    # print(text.get('imdbID'))
    # print(text.get('Poster'))

    # print('>-------->====')

    # IMDBmoviesInfo= []
    # IMDBmoviesInfo.append(text.get('Title'))
    # IMDBmoviesInfo.append(text.get('Year'))
    # IMDBmoviesInfo.append(text.get('Type'))
    # IMDBmoviesInfo.append(text.get('imdbID'))
    # IMDBmoviesInfo.append(text.get('Poster'))

    # context = {

    #     'IMDBmoviesInfo': IMDBmoviesInfo}
        
    # print(IMDBmoviesInfo)
    # print(context)
    # print(IMDBmoviesInfo[0])























    # for result in fielddict:

    #     videosf = {
    #         'Title': result,
    #         'id': result,
    #         'url': f'https://www.imdb.com/title{ result }'
            
    #     }
        # print(video_data)
        # videosf.append(video_data)
    # print(videos)
    


    



#     {"Search":[{"Title":"Avengers: Endgame",
#                  "Year":"2019",
#                "":"tt4154796",
#                  "Type":"movie",
#                "Poster":"https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg"},

#                {"Title":"Avengers: Endgame and the Latest Captain Marvel Outrage!!",
#                  "Year":"2019",
#                "imdbID":"tt10025738",
#                  "Type":"movie",
#                "Poster":"https://m.media-amazon.com/images/M/MV5BZjg2ZTM3OTgtY2ExMS00OGM4LTg3NDEtNjQ0MjJiZDFmMGFkXkEyXkFqcGdeQXVyMDY3OTcyOQ@@._V1_SX300.jpg"},

#                {"Title":"Marvel Studios' Avengers: Endgame LIVE Red Carpet World Premiere",
#                  "Year":"2019",
#                "imdbID":"tt10240638",
#                  "Type":"movie",
#                "Poster":"https://m.media-amazon.com/images/M/MV5BNThjZDgwZTYtMjdmYy00ZmUyLTk4NTUtMzdjZmExODQ3ZmY4XkEyXkFqcGdeQXVyMjkzMDgyNTg@._V1_SX300.jpg"},

#                {"Title":"Avengers Endgame: the Butt Plan",
#                  "Year":"2019",
#                "imdbID":"tt10399328",
#                  "Type":"movie",
#                "Poster":"https://m.media-amazon.com/images/M/MV5BNTQ1OWQzODktMTY3Zi00OTQxLWExOTYtZTNjZjY5ZTY4M2UyXkEyXkFqcGdeQXVyMTAzMzk0NjAy._V1_SX300.jpg"},

#                {"Title":"Avengers: Endgame (2019)",
#                  "Year":"2019",
#                "imdbID":"tt16416424",
#                  "Type":"movie",
#                "Poster":"N/A"},
#                {"Title":"Avengers: Endgame (2019) - Spoiler Full Review",
#                  "Year":"2019",
#                "imdbID":"tt17978032",
#                  "Type":"movie",
#                "Poster":"N/A"}],
#     "totalResults":"6",
#     "Response":"True"}



# {'videos': [{'Title': 'Search', 
#      'id': 'Search', 
#     'url': 'https://www.imdb.com/titleSearch'}, 


#     {'Title': 'totalResults', 
# 'id': 'totalResults', 
# 'url': 'https://www.imdb.com/titletotalResults'},

#  {'Title': 'Response',
#   'id': 'Response', 
# 'url': 'https://www.imdb.com/titleResponse'}]}



















    
# Base url that connects us to the server where the movie info is located
#     url = "https://imdb8.p.rapidapi.com/auto-complete"

# # These headers are used to authenticate your connection
#     headers = {
#     'x-rapidapi-host': "imdb8.p.rapidapi.com",
#     'x-rapidapi-key': ""
#     }

# # These are my keywords I'd like to search for
#     searchTerms = ["spider", "ironman", "avengers", "star wars"]

# # I store all the responses in a list
#     responses = []

# # Here I loop through the search terms
#     for x in range(len(searchTerms)):
#   # Update the searchterm in the url parameters
#         querystring = {"q": searchTerms[x]}

#   # Query the API and save the result
#     response = requests.request("GET", url, headers=headers, params=querystring)

#   # Turn the json text from the response into a useful json python object
#     data = json.loads(response.text)

#   # Format the json to be more readable this is mostly for viewing raw
#   # response data when debugging
#     formattedData = json.dumps(data, indent=4)
#   # Uncomment the following line to see the raw response from the api
#   # print(formattedData)

#   # Load the json data into a dictionary
#     dataDict = json.loads(formattedData)

#   # Save the most important data in our list
#     responses.append(dataDict["d"])

# # Print out the results
#     for x in range(len(searchTerms)):
#         print("\n\nSearch Term: \"" + str(searchTerms[x]) + "\"")
#     for movie in responses[x]:
#         try:
#     # I used try/except here to keep going just incase a movie doesn't have
#     # the data I'm asking for. 
                
#              print("Title: " + movie["l"])
#              print("Image: " + movie["i"]["imageUrl"])
#         except:
#              pass
#     return render(request,'test1.html',querystring)
#     url = "https://moviesdatabase.p.rapidapi.com/titles/search/title/%7Btitle%7D"

#     actors_url="https://moviesdatabase.p.rapidapi.com/actors"

#     # querystring = {"q":"game",
#     #         #         "info": "mini_info",
#     #         #       "limit": "10",
#     #         #        "page": "1", 
#     #         #   "titleType": "movie",
#     #           }

#     headers = {
# 	"X-RapidAPI-Key": "300c876097msha9c4cc55679cfb6p1fe8ccjsn430c7177ad1b",
# 	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
# }

#     searchTerms = ["avengers",]#search

#     response = []

#     # for x in range(len(searchTerms)):
#     querystring = {"q":"game",}



#     response = requests.request(
#         "GET", url, headers=headers, params=querystring)#save the result,send request

#     data = json.loads(response.text)    #turn the json text from the response into a useful json python object

#     #format the json to be more readable this is mostly for viewing raw
#     #response data when debugging
#     formattedData = json.dumps(data,indent=4)
#     #uncomment the following line to see the raw response from the api
#     print(formattedData)

#     # print(response.text)
        




































# {"d":[{"i":{"height":1500,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_.jpg",
# "width":1102},
# "id":"tt0944947",
# "l":"Game of Thrones",
# "q":"TV series",
# "rank":22,
# "s":"Emilia Clarke, Peter Dinklage",
# "v":[{"i":{"height":720,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BZTg4YzdjNTctNDg5Mi00ZmU1LTkzOWEtNmMyNDBjZjNhNTJiXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg",
# "width":1280},
# "id":"vi59490329",
# "l":"Official Series Trailer",
# "s":"3:19"},
# {"i":{"height":1080,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BMmI5YmJmMmEtYWZhOC00M2NhLTg0MjItYjZiMzM1YjdiOWE5XkEyXkFqcGdeQWFsZWxvZw@@._V1_.jpg",
# "width":1920},
# "id":"vi1149616665",
# "l":"All About \"House of the Dragon\"",
# "s":"2:07"},
# {"i":{"height":720,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BMTg0ODM4NTc3OV5BMl5BanBnXkFtZTgwODAwODE1OTE@._V1_.jpg",
# "width":1280},
# "id":"vi2166011673",
# "l":"Season 7 In-Production Teaser",
# "s":"2:03"}],


# "vt":298,"y":2011,"yr":"2011-2019"},
# {"id":"tt21073266",
# "l":"Untitled Jon Snow/Game of Thrones Spinoff",
# "q":"TV series",
# "rank":7234,
# "s":"Kit Harington"},
# {"i":{"height":500,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BYTM3N2ZiZTgtYjlhOC00NGI2LTk5MWItNDBiOGVhZmNhMzZkXkEyXkFqcGdeQXVyMTEwNDU1MzEy._V1_.jpg",
# "width":500},
# "id":"tt13380510",
# "l":"Game of Thrones",
# "q":"video",
# "rank":10256,
# "s":"Roy Dotrice",
# "y":2003},
# {"i":{"height":750,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BODg5NDJhMjYtMTYyYi00NzAwLTliNmYtNGZhMjQ4ZjNkMjgyXkEyXkFqcGdeQXVyNTA3MTU2MjE@._V1_.jpg",
# "width":1334},
# "id":"tt6857128",
# "l":"Unaired Game of Thrones Prequel Pilot",
# "q":"TV movie",
# "rank":10329,
# "s":"Jamie Campbell Bower, Georgie Henley",
# "y":2019},
# {"i":{"height":898,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BODg0YTM4NzEtZDQyNi00M2MzLWE3MDQtNjcxNTkxNWM0NzNhXkEyXkFqcGdeQXVyMjM5NzU3OTM@._V1_.jpg",
# "width":640},
# "id":"tt3391176",
# "l":"Game of Thrones: A Telltale Games Series",
# "q":"video game",
# "rank":24805,
# "s":"Adventure, Drama, Fantasy",
# "y":2014},
# {"i":{"height":1200,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BZDdlMzQzNDQtNTAxMS00NTMyLTgxYTAtYzQ0OGI1YzZhY2Y3XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg",
# "width":810},
# "id":"tt10090796",
# "l":"Game of Thrones: The Last Watch",
# "q":"TV movie",
# "rank":26003,
# "s":"Kevin Alexander, Alfie Allen",
# "y":2019},
# {"i":{"height":840,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BMGYzNDJiOTgtN2Y1OC00NmM2LTk3MTMtZmFhNmJlMzQzNGNhXkEyXkFqcGdeQXVyNDgyODgxNjE@._V1_.jpg",
# "width":600},
# "id":"tt7937220",
# "l":"Game of Thrones Conquest & Rebellion: An Animated History of the Seven Kingdoms",
# "q":"video",
# "rank":31543,
# "s":"Pilou Asbæk, Nikolaj Coster-Waldau",
# "y":2017},

# {"i":{"height":2358,
# "imageUrl":"https://m.media-amazon.com/images/M/MV5BMmYyOTgwYWItYmU3Ny00M2E2LTk0NWMtMDVlNmQ0MWZiMTMxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
# "width":1580},
# "id":"tt0107207",
# "l":"In the Name of the Father",
# "q":"feature",
# "rank":4481,
# "s":"Daniel Day-Lewis, Pete Postlethwaite",
# "y":1993}],
# "q":"game of thr",
# "v":1}


# {"id":"/title/tt0944947/",
# "base":{"@type":"imdb.api.title.base",
# "id":"/title/tt0944947/",
# "image":{"height":1500,
# "id":"/title/tt0944947/images/rm4204167425",
# "url":"https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_.jpg",
# "width":1102},
# "title":"Game of Thrones",
# "titleType":"tvSeries",
# "year":2011},
# "plots":[{"id":"/title/tt0944947/plot/po2596634",
# "text":"Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia."},
# {"author":"Sam Gray",
# "id":"/title/tt0944947/plot/ps2733843",
# "text":"In the mythical continent of Westeros, several powerful families fight for control of the Seven Kingdoms. As conflict erupts in the kingdoms of men, an ancient enemy rises once again to threaten them all. Meanwhile, the last heirs of a recently usurped dynasty plot to take back their homeland from across the Narrow Sea."},
# {"author":"Gregory Tobin",
# "id":"/title/tt0944947/plot/ps3354153",
# "text":"Years after a rebellion spurred by a stolen bride to be and the blind ambitions of a mad King, Robert of the house Baratheon (Mark Addy) sits on the much desired Iron Throne. In the mythical land of Westeros, nine noble families fight for every inch of control and every drop of power. The King's Hand, Jon Arryn (Sir John Standing), is dead. And Robert seeks out his only other ally in all of Westeros, his childhood friend Lord Eddard \"Ned\" Stark. The solemn and honorable Warden of the North is tasked to depart his frozen sanctuary and join the King in the capital of King's Landing to help the now overweight and drunk Robert rule. However, a letter in the dead of night informs \"Ned\" that the former Hand was murdered, and that Robert will be next. So noble Ned goes against his better desires in an attempt to save his friend and the kingdoms. But political intrigue, plots, murders, and sexual desires lead to a secret that could tear the Seven Kingdoms apart. And soon Eddard will find out what happens when you play the Game of Thrones."},
# {"author":"ahmetkozan",
# "id":"/title/tt0944947/plot/ps3913978",
# "text":"Based on the best-selling book series \"A Song of Ice and Fire\" by George R.R. Martin, this sprawling HBO drama is set in a world where summers span several decades and winters can last a lifetime. From the scheming south and the savage eastern lands, to the frozen north and ancient Wall that protects the realm from the mysterious darkness beyond, the powerful families of the Seven Kingdoms are locked in a battle for the Iron Throne. This is a story of duplicity and treachery, nobility and honor, conquest and triumph. In the Game of Thrones, you either win or you die."},
# {"author":"mwitamaibuni",
# "id":"/title/tt0944947/plot/ps6241731",
# "text":"In the mythical continent of Westeros, nine families of higher nobility (Targaryen, Lannisters, Starks, Tyrell, Martell, Greyjoys, Baratheons and Boltons) scramble bitterly to gain power over the seven kingdoms and the Iron throne. As Westeros becomes rife with political unrests, conflicts, treachery, murder and debauchery, an ancient enemy (Army of the dead) awakens and strike the sense of doom to the living folks of Westeros."},
# {"author":"Tfilm78 and Cajunman",
# "id":"/title/tt0944947/plot/ps0207914",
# "text":"Nine noble families fight for control of the mythical land of Westeros. Political and sexual intrigue is pervasive. Robert Baratheon (Mark Addy), King of Westeros, asks his old friend, Lord Eddard Stark (Sean Bean), to serve as Hand of the King, or highest official. Secretly warned that the previous Hand was assassinated, Eddard accepts in order of business to investigate further. Meanwhile, Queen Cersei Lannister's family may be hatching a plot to take power. Across the sea, the last members of the previous and deposed ruling family, the Targaryens, are also scheming to regain the throne. The friction between the houses Stark, Lannister, Baratheon, and Targaryen and with the remaining great houses Greyjoy, Tully, Arryn, Tyrell, and Martell leads to full-scale war. All while an ancient evil awakens in the farthest north. Amidst the war and political confusion, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond."}]}































#test>---------------------------------------------
#     
#     moviesDB = imdb.IMDb()
#     # test=dir(moviesDB)
#     # print(dir(moviesDB))

#     #search for a title
#     movies = moviesDB.search_movie('inception')
#     print('searching for "inception"')
#     for movie in movies:
#         title = movie['title']
#         year = movie['year']

#         print(f'{title}-{year}')
#         test=(f'{title}-{year}')
# #>---------------------------------list movies info
#     # return render(request, 'test1.html',moviesDB)

#     id = movies[0].getID()
#     movie = moviesDB.get_movie(id)
#     title = movie['title']
#     year = movie['year']
#     rating = movie['rating']
#     directors = movie['directors']
#     casting = movie['cast']

#     print('Movie info:')
#     print(f'{title}-{year}')
#     print(f'rating: {rating}')

#     direcStr = ''.join(map(str,directors))
#     print(f'directors: {direcStr}')

#     actors = ','.join(map(str,casting))
#     print(f'actors:{actors}')
   # return HttpResponse(test)
#>-----------------------------------list actor info

    



# def movies():
#     moviesDB = imdb.IMDb()
#     print(moviesDB)

# movies()



#     url = "https://online-movie-database.p.rapidapi.com/auto-complete"

#     querystring = {
#         "q":"giao",
#         'maxResults' : 1,
#     }

#     headers = {
# 	"X-RapidAPI-Key": "0a952dfc75mshbffb8cda5ffcbf8p112dcdjsnd7e8e0ce4569",
# 	"X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
# }

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     response.json()

#     print(response.text)
#     print(response.json())


























# titleType":
# {"text":"Movie","id":"movie","isSeries":false,"isEpisode":false,"__typename":"TitleType"},"titleText":
# {"text":"Not About a Title","__typename":"TitleText"},
# "releaseYear":{"year":2019,"endYear":null,"__typename":"YearRange"},
# "releaseDate":
# {"day":19,"month":6,"year":2019,"__typename":"ReleaseDate"}},{"id":"tt18808946","primaryImage":null,"titleType":{"text":"Movie","id":"movie","isSeries":false,"isEpisode":false,"__typename":"TitleType"},"titleText":{"text":"Title Fight","__typename":"TitleText"},"releaseYear":null,"releaseDate":null},{"id":"tt17537948","primaryImage":null,"titleType":{"text":"Movie","id":"movie","isSeries":false,"isEpisode":false,"__typename":"TitleType"},
# "titleText":
# {"text":"Title Merge","__typename":"TitleText"},"releaseYear":null,"releaseDate":null},{"id":"tt7311992","primaryImage":null,"titleType":
# {"text":"Movie","id":"movie","isSeries":false,"isEpisode":false,"__typename":"TitleType"},"titleText":{"text":"Working Title","__typename":"TitleText"},"releaseYear":null,"releaseDate":null},{"id":"tt7208118","primaryImage":null,"titleType":{"text":"Movie","id":"movie","isSeries":false,"isEpisode":false,"__typename":"TitleType"},"titleText":{"text":"Undisclosed Title","__typename":"TitleText"},"releaseYear":null,"releaseDate":null},{"id":"tt3667646","primaryImage":null,"titleType":{"text":"Movie","id":"movie","isSeries":false,"isEpisode":false,"__typename":"TitleType"},"titleText":{"text":"Undisclosed Title","__typename":"TitleText"},"releaseYear":null,"releaseDate":null},{"id":"tt13348040","primaryImage":null,"titleType":{"text":"Movie","id":"movie","isSeries":false,"isEpisode":false,"__typename":"TitleType"},"titleText":{"text":"Unknown Title","__typename":"TitleText"},"releaseYear":null,"releaseDate":null},{"id":"tt13236364","primaryImage":null,
# "titleType":{"text":"Movie","id":"movie","isSeries":false,"isEpisode":false,"__typename":"TitleType"},
# "titleText":{"text":"Salvage Title","__typename":"TitleText"},"releaseYear":null,"releaseDate": null}]}

























# text=fielddict['d'][0]
   
    # print(fielddict.get('d')[0]['i'])#{'height': 2048, 'imageUrl': 'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg', 'width': 1382}
    # print(fielddict.get('d')[0]['id'])#tt4154796
    # print(fielddict.get('d')[0]['l'])#Avengers: Endgame
    # print(fielddict.get('d')[0]['q'])#feature
    # print(fielddict.get('d')[0]['rank'])#157
    # print(fielddict.get('d')[0]['s'])#Robert Downey Jr., Chris Evans


    # print(fielddict.get('d')[0]['v'][0]["i"]['height'])#1080
    # print(fielddict.get('d')[0]['v'][0]["i"]['imageUrl'])#https://m.media-amazon.com/images/M/MV5BOThlNjdhZmQtNzlkOS00M2VjLWI0ZjUtZDExZDI1MjRhZGFkXkEyXkFqcGdeQW1yb3NzZXI@._V1_.jpg
    # print(fielddict.get('d')[0]['v'][0]['i']['width'])#1920

    # print(fielddict.get('d')[0]['v'][0]['id'])#vi2163260441
    # print(fielddict.get('d')[0]['v'][0]['l'])#"Policy" Trailer
    # print(fielddict.get('d')[0]['v'][0]['s'])#1:06

    # print(fielddict.get('d')[0]['v'][1]["i"]['height'])#1080
    # print(fielddict.get('d')[0]['v'][1]["i"]['imageUrl'])#https://m.media-amazon.com/images/M/MV5BZTFiN2Y4NzEtNDBiNC00MGRiLWFjODAtMzFiYTY2NmE5YmZhXkEyXkFqcGdeQWplZmZscA@@._V1_.jpg
    # print(fielddict.get('d')[0]['v'][1]["i"]['width'])#1920
    # print(fielddict.get('d')[0]['v'][1]["id"])#vi2232337177
    # print(fielddict.get('d')[0]['v'][1]["l"])#The 6 Most Romantic Moments in the Marvel Cinematic Universe
    # print(fielddict.get('d')[0]['v'][1]["s"])#1:48

    # print(fielddict.get('d')[0]['v'][2]["i"]['height'])#1080
    # print(fielddict.get('d')[0]['v'][2]["i"]["imageUrl"])#https://m.media-amazon.com/images/M/MV5BZTNhMWM0M2ItMDY1Ny00MmQ5LWI3N2QtYmY4Njc2MWEyMTYzXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg
    # print(fielddict.get('d')[0]['v'][2]["i"]["width"])#1920
    # print(fielddict.get('d')[0]['v'][2]["id"])#vi1865596185
    # print(fielddict.get('d')[0]['v'][2]["l"])#"Stakes" Featurette
    # print(fielddict.get('d')[0]['v'][2]["s"])#1:01
    # print(fielddict.get('d')[0]['vt'])#117
    # print(fielddict.get('d')[0]['y'])#2019