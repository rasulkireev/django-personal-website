from django.views.generic import CreateView, TemplateView # This is specific to this tutorial https://djangoforbeginners.com/pages-app/ . Learn about these built-in functions
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.syndication.views import Feed

from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

import requests

from writings.models import Post
from newsletter.models import Email
from .forms import NewsletterSignupHomeForm

class HomePageView(TemplateView):
    template_name = "home.html"
    form_class = NewsletterSignupHomeForm
    model = Email
    success_message = "Thanks for signing up...."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(draft=False).order_by('-date')[0:5]

        return context

    
class EmailFormView(SuccessMessageMixin, CreateView):
    form_class = NewsletterSignupHomeForm
    model = Email

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        self.object = form.save()
        
        emailoctopus_api_key = settings.EMAILOCTOPUS_API
        list_id = settings.OCTO_LIST_ID

        data = {
            "api_key": emailoctopus_api_key,
            "email_address": self.object.user_email
        }

        response = requests.post(f"https://emailoctopus.com/api/1.5/lists/{list_id}/contacts", data=data)
        response.status_code
        messages.success(self.request, 'Thanks for signing up!')
        
        return HttpResponseRedirect(reverse_lazy('home'))


class AboutPageView(TemplateView):
    template_name = 'about.html'

class FavouritePageView(TemplateView):
    template_name = 'favourites.html'


class WritingsFeed(Feed):
    title = "Rasul Kireev | Writintgs"
    link = "/rss/"

    def items(self):
        return Post.objects.filter(draft="False").order_by('-date')
   
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.date



class ExperimentsPageView(TemplateView):
    template_name = 'experiments/experiments-list.html'

class FirstD3PageView(TemplateView):
    template_name = 'experiments/first-d3-chart.html'