from django.shortcuts import render,redirect
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
      myform=form.save(commit=False)
      myform.author = request.user
      myform.save()
      return redirect('/')
  else:
    form = PostForms()
  return render(request,'addpost.html',{'form':form})




def editpost(request,id):
  post = Post.objects.get(id=id)
  if request.method == "POST":
    form = PostForms(request.POST,request.FILES,instance=post)
    if form.is_valid():
      myform=form.save(commit=False)
      myform.author = request.user
      myform.save()
      return redirect('/')
  else:
    form = PostForms(instance=post)
  return render(request,'editpost.html',{'form':form})

def deletepost(request,id):
  post=Post.objects.get(id=id)
  post.delete()
  return redirect('/')