from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book


class AllBooksView(ListView):
    model = Book
    template_name = 'books/all.html'

class BooksDetailView(DetailView): # new
    model = Book
    template_name = 'books/book.html'
