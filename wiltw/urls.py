from django.urls import path
from .views import WiltwListView, WiltwDetailView, WiltwLatestView

urlpatterns = [
        path('archive', WiltwListView.as_view(), name='wiltw-archive'),
        path('archive/<int:pk>', WiltwDetailView.as_view(), name='wiltw-then'),
        path('', WiltwLatestView.as_view(), name='wiltw-now'),
            ]
