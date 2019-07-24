from django.urls import path
from .views import AllBooksView, BooksDetailView

urlpatterns = [
        path('', AllBooksView.as_view(), name='all_books'),
        path('<slug:slug>', BooksDetailView.as_view(), name='book'),
            ]
