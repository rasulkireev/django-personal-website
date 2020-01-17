from django.urls import path
from .views import HomePageView, AboutPageView, WritingsFeed

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('rss.xml', WritingsFeed(), name='writings-rss'),
]
