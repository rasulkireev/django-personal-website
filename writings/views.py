from django.contrib.syndication.views import Feed
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse
from mentions.models.webmention import Webmention
from mentions.tasks.outgoing_webmentions import process_outgoing_webmentions


class PostListView(ListView):
    model = Post
    template_name = 'writings/all_posts.html'
    ordering = '-date'

class PostDetailView(DetailView):
    model = Post
    template_name = 'writings/post.html'

    def get_context_data(self, **kwargs):
        current_post = Post.objects.get(slug=self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context ['webmentions'] = Webmention.objects.all()

        return context

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post', kwargs = {'slug':self.object.post.slug})
        
    def form_valid(self, form):
        current_post = Post.objects.get(slug=self.kwargs['slug'])
        form.instance.slug = current_post.slug
        form.instance.post_id = current_post.id
        return super(AddComment, self).form_valid(form)
        
class DjangoLatestEntriesFeed(Feed):
    title = "Django Writintgs"
    link = "/djangofeed/"
    description = "These are posts about my experiences learning and working with Django."

    def items(self):
        return Post.objects.filter(category="Django", draft="False").order_by('-date')
        
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.date
