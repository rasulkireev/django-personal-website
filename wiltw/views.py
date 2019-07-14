from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Wiltw


class WiltwListView(ListView):
    model = Wiltw
    template_name = 'wiltw/wiltw-archive.html'
    ordering = '-title'

class WiltwDetailView(DetailView): # new
    model = Wiltw
    template_name = 'wiltw/wiltw-then.html'

class WiltwLatestView(DetailView): # new
    model = Wiltw
    template_name = 'wiltw/wiltw-now.html'

    def get_object(self):
        return Wiltw.objects.order_by('-title').first()
