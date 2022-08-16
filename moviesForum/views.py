from django.shortcuts import render

from moviesForum.models import Reply

from moviesList.models import BlogPost, moviesInformation,userinformation
from user.models import MySession
from user.models import userinformation as User
# from user.views import getSession

from django.http import Http404
# Create your views here.
from django.shortcuts import render, redirect

def index(request):
    """ 首页 GET """
    # 将所有帖子按时间排序
    topics = BlogPost.objects.order_by('-publish_date')
    # userid=request.POST['userid']

    if request.user.is_authenticated:
    # 用户已登陆
     print('yidenglu1')
    else:
    # 用户未登陆
        print('[][][][]')
    userid=request.user.userid
    print('...................',userid)
        
    


   
    return render(request, 'indexBlog.html', {
                                    "topics": topics,
        "stats": {
            "users": userinformation.objects.count(),
            "topics": BlogPost.objects.count(),
            "replies": Reply.objects.count()
        },
        # "topped_topics": BlogPost.objects.filter(BlogPostTop=True).order_by('-publish_date')
    })

import requests
def create(request):
    """ 创建帖子 GET/POST """
    if request.method == "GET":
        print('get方法')
        if request.user.is_authenticated:
            print('用户存在')
            return render(request, 'create.html', {"logged_in_user": request.user })
            
        else:
            return redirect('/login/')
    elif request.method == "POST":
        if request.user.is_authenticated:
            BlogPosttitle = request.POST.get('title')
            BlogPostcontent = request.POST.get('content')
            BlogId = User.objects.filter(userid=request.user.userid).first()
            

            url = "https://badword.p.rapidapi.com/"

            querystring = {"content":"fuck"}
            querystring["content"] = BlogPostcontent = request.POST.get('content')


            headers = {
	"X-RapidAPI-Key": "300c876097msha9c4cc55679cfb6p1fe8ccjsn430c7177ad1b",
	"X-RapidAPI-Host": "badword.p.rapidapi.com"
}

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)

            badWord=response.json()
            
            # movie=moviesInformation.objects.filter(movies_title=str(BlogPosttitle)).first()
            # movieid=movie.id

            if BlogPosttitle == "" or BlogPostcontent == "":
                return render(request, 'create.html', {
                    "error": "You have no input!",
                    "logged_in_user": request.user
                })
            else:
                print('is_bad',badWord['is-bad'])
                if badWord['is-bad']==True:
                    return render(request, 'create.html', {
                        "error": "There are inappropriate words in the content you are about to post.",
                        "logged_in_user": request.user
                    })


            BlogPost1 = BlogPost(movie_id=1,title=BlogPosttitle,  body=BlogPostcontent, user_id=BlogId)
            BlogPost1.save()
            print('文章已保存')
        else:
            return redirect('http://localhost:8000/user/login/')
        # return redirect('')
        return redirect('http://localhost:8000/moviesForum/index/')


def topic(request,Blog_id):
    """ 帖子 GET """
    try:
        topic = BlogPost.objects.get(id=Blog_id)
    except:
        raise Http404("帖子不存在")
    
    
    return render(request, 'topic.html', {
        "topic": topic,
        "replies": Reply.objects.filter(reply_Blog=Blog_id),
        
    })



def reply(request, Blog_id):
    """ 回复 POST """
    if request.method == "POST":
        if request.user.is_authenticated:
            form_content = request.POST.get('content')
            form_author = User.objects.filter(username=request.user).first()
            form_topic = BlogPost.objects.filter(id=Blog_id).first()

            if form_content != "":
                reply = Reply(reply_body=form_content, reply_user=form_author, reply_Blog=form_topic)
                reply.save()
                print('使用了reply')
            
            return redirect('http://localhost:8000/moviesForum/index/topic/{}/'.format(Blog_id))
            
        else:
            return redirect('/login/')