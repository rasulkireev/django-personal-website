from django.urls import path
from .views import PostListView, PostDetailView, DjangoLatestEntriesFeed, WritingsFeed

urlpatterns = [
        path('', PostListView.as_view(), name='all_posts'),
        path('<slug:slug>', PostDetailView.as_view(), name='post'),
        path('django-feed/rss/', DjangoLatestEntriesFeed()),
        path('feed/rss/', WritingsFeed())
            ]
