#from django.contrib.auth.models import AbstractUser
from tabnanny import verbose
from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length=11,unique=True)
    icon = models.ImageField(upload_to='imgurl/%Y/%m/%d')

    class Mate:
        db_table='user'
        verbose_name = '用户表'
