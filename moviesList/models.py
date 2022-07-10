

from django.db import models
MEDIA_ADDR = 'http://localhost:8000/media/'
# Create your models here.
class moviesInfo(models.Model):
    movies_name = models.CharField(max_length=32,verbose_name='moviename',null=True)#如果是charfield 必须写max_length
    
    classification = models.CharField(max_length=32,null=True,blank=True)#分类
    release_data = models.DateTimeField(null=True,blank=True)#上映时间
    movies_rating = models.IntegerField(default=2)#电影评分
   # account=models.DecimalField(max_digits=10,decimal_places=2,default=0)#decimal保留两位小数
    movies_posts = models.DateTimeField(verbose_name='时间')#添加新字段需要在sql上同步
    img_url = models.ImageField(upload_to='imgurl/',verbose_name=u'img')
    
    def __str__(self):
        return self.movies_name

    def get_img_url_url(self):
        return MEDIA_ADDR + str(self.img_url)
#该拿图片了


