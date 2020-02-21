from django.urls import path
from .views import ReadBooksView, CurrentlyReadingBooksView, ToReadBooksView, BooksDetailView

urlpatterns = [
        path('', ReadBooksView.as_view(), name='read-books'),
        path('to-read', ToReadBooksView.as_view(), name='to-read-books'),
        path('reading', CurrentlyReadingBooksView.as_view(), name='currently-reading-books'),
        
        path('<slug:slug>', BooksDetailView.as_view(), name='book'),
            ]
