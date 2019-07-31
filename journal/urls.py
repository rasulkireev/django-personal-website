from django.urls import path
from .views import JournalEntry

urlpatterns = [
        path('', JournalEntry.as_view(), name='journal'),
            ]
