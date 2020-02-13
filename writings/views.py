import os
import json
import uuid

from django.contrib.syndication.views import Feed
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.http import HttpResponse

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .models import Post, Book
from .forms import NewsletterSignupPostForm
from newsletter.forms import NewsletterSignupForm
from newsletter.models import Email

from mentions.models.webmention import Webmention
from mentions.tasks.outgoing_webmentions import process_outgoing_webmentions

from martor.utils import LazyEncoder


class PostListView(ListView):
    model = Post
    template_name = 'writings/posts/all-posts.html'
    ordering = '-date'

class PostDetailView(DetailView):
    model = Post
    template_name = 'writings/posts/post.html'

    def get_context_data(self, **kwargs):
        current_post = Post.objects.get(slug=self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context['webmentions'] = Webmention.objects.all()
        context['email_form'] = NewsletterSignupPostForm

        return context

class EmailFormView(SuccessMessageMixin, CreateView):
    form_class = NewsletterSignupPostForm
    model = Post
    success_message = "Thanks for signing up!"
    
    def get_success_url(self):
        return reverse('post', kwargs = {'slug':self.object.slug})

    def form_valid(self, form):
        current_post = Post.objects.get(slug=self.kwargs['slug'])
        form.instance.slug = current_post.slug
        form.instance.post_id = current_post.id
        return super(EmailFormView, self).form_valid(form)




class ReadBooksView(ListView):
    model = Book
    template_name = 'writings/books/all-books.html'
    ordering = '-date_read'
    queryset = Book.objects.filter(status="READ")

class BooksDetailView(DetailView):
    model = Book
    template_name = 'writings/books/book.html'




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

@login_required
def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            img_uuid = "{0}-{1}".format(uuid.uuid4().hex[:10], image.name.replace(' ', '-'))
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL, def_path)

            data = json.dumps({
                'status': 200,
                'link': img_url,
                'name': image.name
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))