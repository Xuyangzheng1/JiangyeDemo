from ast import Param
import json
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

   #https://rapidapi.com/rapidapi/api/movie-database-alternative/

    url = "https://movie-database-alternative.p.rapidapi.com/"

    querystring = {"s":"Avengers Endgame",
    "r":"json",
    "page":"1"}

    headers = {
	"X-RapidAPI-Key": "300c876097msha9c4cc55679cfb6p1fe8ccjsn430c7177ad1b",
	"X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
}

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    fielddict = response.json()
    
    return render(request,'test1.html',{'field':fielddict})

















    {"Search":[{"Title":"Avengers: Endgame",
    "Year":"2019",
    "imdbID":"tt4154796",
    "Type":"movie",
    "Poster":"https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg"},
    {"Title":"Avengers: Endgame and the Latest Captain Marvel Outrage!!",
    "Year":"2019",
    "imdbID":"tt10025738",
    "Type":"movie",
    "Poster":"https://m.media-amazon.com/images/M/MV5BZjg2ZTM3OTgtY2ExMS00OGM4LTg3NDEtNjQ0MjJiZDFmMGFkXkEyXkFqcGdeQXVyMDY3OTcyOQ@@._V1_SX300.jpg"},
    {"Title":"Marvel Studios' Avengers: Endgame LIVE Red Carpet World Premiere",
    "Year":"2019",
    "imdbID":"tt10240638",
    "Type":"movie",
    "Poster":"https://m.media-amazon.com/images/M/MV5BNThjZDgwZTYtMjdmYy00ZmUyLTk4NTUtMzdjZmExODQ3ZmY4XkEyXkFqcGdeQXVyMjkzMDgyNTg@._V1_SX300.jpg"},
    {"Title":"Avengers Endgame: the Butt Plan",
    "Year":"2019",
    "imdbID":"tt10399328",
    "Type":"movie",
    "Poster":"https://m.media-amazon.com/images/M/MV5BNTQ1OWQzODktMTY3Zi00OTQxLWExOTYtZTNjZjY5ZTY4M2UyXkEyXkFqcGdeQXVyMTAzMzk0NjAy._V1_SX300.jpg"},
    {"Title":"Avengers: Endgame (2019)",
    "Year":"2019",
    "imdbID":"tt16416424",
    "Type":"movie",
    "Poster":"N/A"},
    {"Title":"Avengers: Endgame (2019) - Spoiler Full Review",
    "Year":"2019",
    "imdbID":"tt17978032",
    "Type":"movie",
    "Poster":"N/A"}],
    "totalResults":"6",
    "Response":"True"}
    
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