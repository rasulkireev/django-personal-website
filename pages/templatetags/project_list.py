from django import template

register = template.Library()

from projects.models import Project

@register.inclusion_tag('template_tags/project_list.html')
def hustles(project):
  project = Project.objects.filter(project_type="Hustle")
  return {'project': project}

@register.inclusion_tag('template_tags/project_list.html')
def projects(project):
  project = Project.objects.filter(project_type="Project")
  return {'project': project}
