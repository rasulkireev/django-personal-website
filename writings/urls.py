from django.urls import path
from .views import (PostListView, 
                    PostDetailView, 
                    DjangoLatestEntriesFeed, 
                    EmailFormView,
                    ReadBooksView,
                    BooksDetailView)


urlpatterns = [
    path('posts', PostListView.as_view(), name='all_posts'),
    path('posts/<slug:slug>', PostDetailView.as_view(),kwargs={'model_name': 'writings.Post'}, name='post'),
    
    path('books', ReadBooksView.as_view(), name='all-books'),
    path('books/<slug:slug>', BooksDetailView.as_view(), name='book'),

    path('django-feed/rss/', DjangoLatestEntriesFeed(), name='django-rss'),

    path('<slug:slug>/newsletter', EmailFormView.as_view(), name='post-newsletter'),
]
