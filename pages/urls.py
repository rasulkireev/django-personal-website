from django.urls import path
from .views import HomePageView, AboutPageView, FavouritePageView, WritingsFeed

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('favourites/', FavouritePageView.as_view(), name='favourites'),
    path('rss.xml', WritingsFeed(), name='writings-rss'),
]
