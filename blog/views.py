from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForms
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
# Create your views here.


class Post_list(ListView):
  model = Post
  template_name = 'index.html'
  context_object_name = 'post'



class Post_detail(DetailView):

  model = Post
  template_name = 'postdetail.html'
  context_object_name = 'post'



class Post_create(CreateView):
  model = Post
  template_name = 'addpost.html'
  fields = ['title','cotent','date_post','image','draft','tag','author']
  success_url = '/'
  



class Post_edit(UpdateView):
  model = Post
  template_name = 'editpost.html'
  fields = ['title','cotent','date_post','image','draft','tag','author']
  success_url = '/'




class Post_delet(DeleteView):
  model = Post
  success_url = '/'

