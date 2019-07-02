from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class WiltwListView(ListView):
    model = Post
    template_name = 'wiltw/wiltw-archive.html'

class WiltwDetailView(DetailView): # new
    model = Post
    template_name = 'wiltw/wiltw-then.html'

class WiltwLatestView(DetailView): # new
    model = Post
    template_name = 'wiltw/wiltw-now.html'

    def get_object(self):
        return Post.objects.order_by('-title').first()
