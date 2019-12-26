from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book


class ReadBooksView(ListView):
    model = Book
    template_name = 'books/read-books.html'
    ordering = '-date_read'
    queryset = Book.objects.filter(status="READ")

class CurrentlyReadingBooksView(ListView):
    model = Book
    template_name = 'books/currently-reading.html'
    ordering = '-date_read'
    queryset = Book.objects.filter(status="READING")

class ToReadBooksView(ListView):
    model = Book
    template_name = 'books/to-read.html'
    ordering = '-date_read'
    queryset = Book.objects.filter(status="TO READ")


class BooksDetailView(DetailView): # new
    model = Book
    template_name = 'books/book.html'
