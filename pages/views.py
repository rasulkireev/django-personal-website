from django.shortcuts import render
from django.views.generic import TemplateView #This is specific to this tutorial https://djangoforbeginners.com/pages-app/ . Learn about these built-in functions

class HomePageView(TemplateView):
    template_name = 'home.html'

class NowPageView(TemplateView):
    template_name = 'now.html'
