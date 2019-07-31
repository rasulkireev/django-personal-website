from django.shortcuts import render
from django.views.generic import ListView
from .models import Journal


class JournalEntry(ListView):
    model = Journal
    template_name = 'journal/home.html'
