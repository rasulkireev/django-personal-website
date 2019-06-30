from django.urls import path
from .views import NowListView, NowDetailView, NowLatestView

urlpatterns = [
        path('archive', NowListView.as_view(), name='archive'),
        path('archive/<int:pk>', NowDetailView.as_view(), name='then'),
        path('', NowLatestView.as_view(), name='now'),
            ]
