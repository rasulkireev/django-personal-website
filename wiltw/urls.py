from django.urls import path
from .views import WiltwListView, WiltwDetailView, WiltwLatestView

urlpatterns = [
        path('archive', WiltwListView.as_view(), name='wiltw_archive'),
        path('archive/<slug:slug>', WiltwDetailView.as_view(), name='wiltw_then'),
        path('', WiltwLatestView.as_view(), name='wiltw_now'),
            ]
