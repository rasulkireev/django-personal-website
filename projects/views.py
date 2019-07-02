from django.views.generic import ListView
from .models import Post


class ProjectList(ListView):
    model = Post
    template_name = 'projects/home.html'
