from django.shortcuts import render
from .models import Post
# Create your views here.

def Post_list(requset):
  
  post=Post.objects.all()
  return render(requset,'index.html',{'post':post})



def post_detail(request,id):
  post = Post.objects.get(id=id)

  return render(request,'postdetail.html',{'post':post})