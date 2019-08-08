from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'gallery/gallery.html'


class PhotoDetailView(DetailView): # new
    model = Photo
    template_name = 'gallery/photo.html'
