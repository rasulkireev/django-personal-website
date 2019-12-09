from django.urls import path
from .views import PostListView, PostDetailView, AddComment, DjangoLatestEntriesFeed

urlpatterns = [
        path('', PostListView.as_view(), name='all_posts'),
        path('<slug:slug>', PostDetailView.as_view(), name='post'),
        path('django-rss/latest/feed/', DjangoLatestEntriesFeed()),
        path('<slug:slug>/add', AddComment.as_view(), name='add-comment'),
            ]
