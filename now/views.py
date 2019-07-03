from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Now


class NowListView(ListView):
    model = Now
    template_name = 'now/archive.html'

class NowDetailView(DetailView): # new
    model = Now
    template_name = 'now/then.html'

class NowLatestView(DetailView): # new
    model = Now
    template_name = 'now/now.html'

    def get_object(self):
        return Now.objects.order_by('-title').first()
