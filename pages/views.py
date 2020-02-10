from django.contrib.syndication.views import Feed
from django.shortcuts import render
from django.views.generic import TemplateView # This is specific to this tutorial https://djangoforbeginners.com/pages-app/ . Learn about these built-in functions
from writings.models import Post
from newsletter.forms import NewsletterSignupForm

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(draft=False).order_by('-date')[0:5]
        context['email_form'] = NewsletterSignupForm

        return context


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