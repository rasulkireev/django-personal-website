from django.urls import path
from .views import WeightAPIView


urlpatterns = [
    path('weight/', WeightAPIView.as_view()),
    ]