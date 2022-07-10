import email
from turtle import title
from unicodedata import name
from django.db import models
from pkg_resources import require

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32,verbose_name='usersname',null=True)#如果是charfield 必须写max_length
    password = models.CharField(max_length=32,verbose_name='userpassword',null=True)
    age = models.IntegerField(null=True,blank=False)
    size = models.IntegerField(null=True,blank=False)
    date = models.IntegerField(default=2)
   # account=models.DecimalField(max_digits=10,decimal_places=2,default=0)#decimal保留两位小数
    create_time = models.DateTimeField(null=False,blank=True)#添加新字段需要在sql上同步
    email = models.CharField(max_length=32,verbose_name='email',null=True)

    
    

"""  
create table app01_userinfo(
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
)""" 

class Department(models.Model):
    id= models.BigAutoField(verbose_name='ID自增',primary_key=True)#BigAutoField Id为自增
    title = models.CharField(max_length=16)

class Role(models.Model):
    title = models.CharField(max_length=16)    

#Department.objects.create(title="giaogiao")

#UserInfo.objects.create(name="giaogiao",age=2)
