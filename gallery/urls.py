from django.urls import path
from .views import PhotoListView, PhotoDetailView

urlpatterns = [
        path('', PhotoListView.as_view(), name='gallery'),
        path('<slug:slug>', PhotoDetailView.as_view(), name='photo'),
            ]
