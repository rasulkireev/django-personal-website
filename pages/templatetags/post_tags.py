from django import template

register = template.Library()

from writings.models import Post

@register.inclusion_tag('template_tags/list.html')
def latest_posts(post):
  post = Post.objects.order_by('-date')[0:3]
  return {'post': post}