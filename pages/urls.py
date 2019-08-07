from django.urls import path
from .views import HomePageView, PhotoGalleryView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('photos/', PhotoGalleryView.as_view(), name='photo_gallery'),
]
