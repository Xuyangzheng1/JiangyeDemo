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
    
    topics = BlogPost.objects.order_by('-publish_date')
    # userid=request.POST['userid']

    if request.user.is_authenticated:
    
     print('yidenglu1')
    else:
    
        print('[][][][]')
    userid=request.user.userid
    print('...................',userid)
        
    


   
   
    return render(request, 'testjs.html', {
                                    "topics": topics,
        "stats": {
            "users": userinformation.objects.count(),
            "topics": BlogPost.objects.count(),
            "replies": Reply.objects.count()
        },
        
    })

import requests
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login/', redirect_field_name='testjs/')
def create(request):
    """ Create you blog GET/POST """
    if request.method == "GET":
        print('get')
        if request.user.is_authenticated:
            print('have user')
            return render(request, 'create.html', {"logged_in_user": request.user })
            
        else:
            return redirect('/login/')
    elif request.method == "POST":
        if request.user.is_authenticated:
            BlogPosttitle = request.POST.get('title')
            BlogPostcontent = request.POST.get('content')
            BlogId = User.objects.filter(userid=request.user.userid).first()
            

            url = "https://badword.p.rapidapi.com/"

            querystring = {"content":"1"}
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
            print('saved')
        else:
            return redirect('http://localhost:8000/user/login/')
        # return redirect('')
        return redirect('http://localhost:8000/moviesForum/index/')


def topic(request,Blog_id):
    
    try:
        topic = BlogPost.objects.get(id=Blog_id)
    except:
        raise Http404("no blog")
    
    
    return render(request, 'topic.html', {
        "topic": topic,
        "replies": Reply.objects.filter(reply_Blog=Blog_id),
        
    })



def reply(request, Blog_id):
    
    if request.method == "POST":
        if request.user.is_authenticated:
            content = request.POST.get('content')
            author = User.objects.filter(username=request.user).first()
            topic = BlogPost.objects.filter(id=Blog_id).first()

            url = "https://badword.p.rapidapi.com/"

            querystring = {"content":"1"}
            querystring["content"] = content


            headers = {
	"X-RapidAPI-Key": "300c876097msha9c4cc55679cfb6p1fe8ccjsn430c7177ad1b",
	"X-RapidAPI-Host": "badword.p.rapidapi.com"
}

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)

            badWord=response.json()
            print(badWord)
            chcekBadword = badWord['is-bad']

            if content != "" and chcekBadword!=True:
                print('re')
                reply = Reply(reply_body=content, reply_user=author, reply_Blog=topic)
                reply.save()
                print('reply')
            
            return redirect('http://localhost:8000/moviesForum/index/topic/{}/'.format(Blog_id))
            
        else:
            return redirect('/login/')