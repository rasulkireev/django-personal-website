from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse


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
        context ['comments'] = Comment.objects.filter(post_id=current_post.id)
        context['form'] = CommentForm()
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