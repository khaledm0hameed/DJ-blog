from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User



# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    cotent=models.TextField(max_length=30000)
    date_post=models.DateField(default=timezone.now)
    image=models.ImageField()
    draft=models.BooleanField(default=True)
    tag = TaggableManager()
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)



    def __str__(self):
        
        return self.title