from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
        path('', PostListView.as_view(), name='all_posts'),
        path('<slug:slug>', PostDetailView.as_view(), name='post'),
            ]
