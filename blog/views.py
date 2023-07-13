from django.shortcuts import render
from .models import Post
from .forms import PostForms
# Create your views here.

def Post_list(requset):
  
  post=Post.objects.all()
  return render(requset,'index.html',{'post':post})



def post_detail(request,id):
  post = Post.objects.get(id=id)

  return render(request,'postdetail.html',{'post':post})



def addpost(request):
  if request.method == "POST":
    form = PostForms(request.POST,request.FILES)
    if form.is_valid():
      form.save()
  else:
    form = PostForms()
  return render(request,'addpost.html',{'form':form})

def editpost(request):
  pass

def deletepost(request):
  pass