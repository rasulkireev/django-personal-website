from django.views.generic import ListView
from .models import Project


class ProjectList(ListView):
    model = Project
    template_name = 'projects/home.html'
