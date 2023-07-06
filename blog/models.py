from django.db import models
from django.utils import timezone

def get_current_time():
    current_time = timezone.now()
    return current_time

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    cotent=models.TextField(max_length=30000)
    date_post=models.DateField(default=timezone.now)
    image=models.ImageField()
    draft=models.BooleanField(default=True)