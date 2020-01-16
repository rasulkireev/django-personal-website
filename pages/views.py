from django.shortcuts import render
from django.views.generic import TemplateView # This is specific to this tutorial https://djangoforbeginners.com/pages-app/ . Learn about these built-in functions
from writings.models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(draft=False).order_by('-date')[0:5]

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'
