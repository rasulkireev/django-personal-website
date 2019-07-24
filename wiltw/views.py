from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Wiltw


class WiltwListView(ListView):
    model = Wiltw
    template_name = 'wiltw/wiltw_archive.html'
    ordering = '-title'

class WiltwDetailView(DetailView): # new
    model = Wiltw
    template_name = 'wiltw/wiltw_then.html'

class WiltwLatestView(DetailView): # new
    model = Wiltw
    template_name = 'wiltw/wiltw_now.html'

    def get_object(self):
        return Wiltw.objects.order_by('-title').first()
