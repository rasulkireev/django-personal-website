from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import WeightMeasurement
from django.urls import reverse


class WeightListView(ListView):
    model = WeightMeasurement
    template_name = 'health/health_home.html'
    ordering = '-date_and_time'