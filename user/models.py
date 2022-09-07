#from django.contrib.auth.models import AbstractUser
from distutils.command.upload import upload
from lib2to3.pgen2 import token
from tabnanny import verbose
from django.db import models




# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length=11,unique=True)
    icon = models.ImageField(upload_to='imgurl/%Y/%m/%d')

    class Meta:
        db_table='user'
        verbose_name = '用户表'


import email
from email.policy import default
from turtle import title
from unicodedata import name
from django.db import models
from pkg_resources import require
from django.contrib.auth.models import AbstractUser
from django.contrib import auth

from django.contrib.sessions.models import Session

# Create your models here.
MEDIA_ADDR = 'http://localhost:8000/media/uesrsImg/'

class userinformation(AbstractUser):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,verbose_name='usersname',null=True,unique=True)
    password = models.TextField(max_length=225,verbose_name='userpassword',null=True)
    age = models.IntegerField(null=True,blank=False)
    sex = models.CharField(max_length=10,default='man',verbose_name='sex')
    
   
    create_time = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    email = models.CharField(max_length=32,verbose_name='email',null=True)
    userImg = models.ImageField(upload_to='usersImg',verbose_name=u'img')

    def get_uesrImg_url(self):
        return MEDIA_ADDR + str(self.uesrImg)


class MySession(models.Model):
    token=models.CharField(primary_key=True,max_length=225,verbose_name='token')
    Sessionkey=models.CharField(max_length=225,default='0',verbose_name='Sessionkey')

    class Meta:
        verbose_name_plural = 'MySession'
class WatchMovie(models.Model):
    id=models.CharField(primary_key=True,max_length=225,verbose_name='id')
    movieName=models.CharField(max_length=225,verbose_name='movieName')
    url1=models.CharField(max_length=225,verbose_name='url1')
    url2=models.CharField(max_length=225,verbose_name='url2')
    img=models.CharField(max_length=225,verbose_name='img')
    userId=models.CharField(max_length=225,verbose_name='userId')