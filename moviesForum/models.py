from django.db import models
from moviesList.models import BlogPost

from user.models import userinformation

# Create your models here.
class Reply(models.Model):
    
    reply_user = models.ForeignKey(to=userinformation, on_delete=models.CASCADE, verbose_name="作者")
    reply_body = models.TextField("内容", max_length=4096)
    reply_create_time = models.DateTimeField("创建时间", auto_now_add=True)
    reply_Blog = models.ForeignKey(to=BlogPost, on_delete=models.CASCADE, verbose_name="所在帖子")

    def __str__(self):
        return "#" + str(self.id) + " " + self.reply_user.__str__() + " in blog " + self.reply_Blog.__str__() + " reply " + self.reply_body



