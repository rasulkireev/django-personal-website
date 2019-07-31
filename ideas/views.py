from django.shortcuts import render
from django.views.generic import ListView
from .models import Idea


class AllIdeas(ListView):
    model = Idea
    template_name = 'ideas/home.html'
