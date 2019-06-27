from django.urls import path
from .views import HomePageView, NowPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('now/', NowPageView.as_view(), name='now'),
]
