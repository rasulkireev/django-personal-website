from django.urls import path
from .views import PostListView, PostDetailView, DjangoLatestEntriesFeed

urlpatterns = [
        path('', PostListView.as_view(), name='all_posts'),
        path('<slug:slug>', PostDetailView.as_view(),kwargs={'app_label': 'writings.Post'}, name='post'),
        path('django-feed/rss/', DjangoLatestEntriesFeed(), name='django-rss'),
            ]
