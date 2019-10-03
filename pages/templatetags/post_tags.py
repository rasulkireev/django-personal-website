from django import template

register = template.Library()

from writings.models import Post

@register.inclusion_tag('template_tags/post_list.html')
def latest_posts(post):
  post = Post.objects.filter(draft=False).order_by('-date')[0:6]
  return {'post': post}
