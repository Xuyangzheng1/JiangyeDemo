#from django.contrib.auth.models import AbstractUser
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
MEDIA_ADDR = 'http://localhost:8000/media/'

class userinformation(AbstractUser):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,verbose_name='usersname',null=True,unique=True)#如果是charfield 必须写max_length
    password = models.TextField(max_length=64,verbose_name='userpassword',null=True)#1406 charfied更改为text field
    age = models.IntegerField(null=True,blank=False)
    sex = models.CharField(max_length=10,default='man',verbose_name='sex')
    
   # account=models.DecimalField(max_digits=10,decimal_places=2,default=0)#decimal保留两位小数
    create_time = models.DateTimeField(null=True,blank=True)#添加新字段需要在sql上同步
    email = models.CharField(max_length=32,verbose_name='email',null=True)
    userImg = models.ImageField(upload_to='usersImg/',verbose_name=u'img',default=0)

    def get_uesrImg_url(self):
        return MEDIA_ADDR + str(self.uesrImg)


class MySession(models.Model):
    token=models.CharField(primary_key=True,max_length=225,verbose_name='token')
    Sessionkey=models.CharField(max_length=225,default='0',verbose_name='Sessionkey')

    class Meta:
        verbose_name_plural = 'MySession'