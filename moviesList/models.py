from asyncio.windows_events import NULL
from audioop import reverse
from distutils.text_file import TextFile
from typing import Text
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from user.models import userinformation


MEDIA_ADDR = 'http://localhost:8000/media/'


# Create your models here.
class moviesInformation(models.Model):
    
    user_id = models.ManyToManyField(userinformation)

    movie_imdbid=models.CharField(max_length=1024,verbose_name=' movieimdbid',null=True)
    classification = models.CharField(max_length=32,null=True,blank=True)#分类


    movies_title = models.TextField(max_length=225,verbose_name='moviename',null=True)#如果是charfield 必须写max_length
    movies_language=models.CharField(max_length=32,verbose_name='movielanguage',null=True)
    movies_country=models.CharField(max_length=32,verbose_name='moviecountry',null=True)
    movies_suggestions =models.CharField(max_length=225,verbose_name='moviesuggestions',null=True)
    movies_matlevel =models.CharField(max_length=225,verbose_name='moviesmatlevel',null=True)
    movies_avg_rating = models.IntegerField(default=2)#电影评分
    movie_introduction=models.TextField(max_length=10240,verbose_name='movieintroduction',null=True)
    movie_runtime=models.CharField(max_length=255,verbose_name=' movieruntime',null=True)
    movie_imdblink=models.CharField(max_length=1024,verbose_name=' movieimdblink',null=True)
    movie_natflixlink=models.CharField(max_length=1024,verbose_name=' movienatflixlink',null=True)



    release_data = models.IntegerField(null=True,blank=True,default=2022)#上映时间
    
   # account=models.DecimalField(max_digits=10,decimal_places=2,default=0)#decimal保留两位小数
    movies_add_time = models.DateTimeField(verbose_name='时间',default=timezone.now)#添加新字段需要在sql上同步
    img_url = models.ImageField(upload_to='imgurl/',verbose_name=u'img')



    
    def __str__(self):
        return self.movies_title

    def get_img_url_url(self):
        return MEDIA_ADDR + str(self.img_url)
#该拿图片了



class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    

    def __str__(self): 
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self): 
        return self.title

from tinymce.models import HTMLField

class BlogPost(models.Model):
    title=models.CharField(max_length=255,null=True,verbose_name='movieTitle')
    body=HTMLField()
    save_number = models.IntegerField(verbose_name='save_number',default=0)
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='publish_date')
    user_id = models.ForeignKey(verbose_name="userBlog",to=userinformation,on_delete=models.CASCADE)
    movie = models.ForeignKey(verbose_name="movies",to=moviesInformation,on_delete=models.CASCADE,blank=True)
    BlogPostTop=models.BooleanField("BlogPostTop", default=False)
    class Meta:
        db_table = 'article'
        verbose_name = 'article_table'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


# class BlogPost2(models.Model):
#     title=models.CharField(max_length=255,null=True,verbose_name='movieTitle')

    
#     BlogpostObject = models.OneToOneField(BlogPost,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     movie = models.ForeignKey(verbose_name="movies",to=moviesInformation,on_delete=models.CASCADE,blank=True)

   
    