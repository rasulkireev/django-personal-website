from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'writings/all-posts.html'

class PostDetailView(DetailView): # new
    model = Post
    template_name = 'writings/post.html'

class NowLatestView(ListView):
    model = Post
    #template_name = 'now/now.html'
    context_object_name = 'top3'

    def get_object(self):
        return Post.objects.order_by('-date')[0:3]
