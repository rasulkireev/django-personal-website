from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class NowListView(ListView):
    model = Post
    template_name = 'now/archive.html'

class NowDetailView(DetailView): # new
    model = Post
    template_name = 'now/then.html'

class NowLatestView(DetailView): # new
    model = Post
    template_name = 'now/now.html'

    def get_object(self):
        return Post.objects.order_by('-title').first()
