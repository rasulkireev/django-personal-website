from django.urls import path
from .views import WritingsAPIView


urlpatterns = [
    path('writings/', WritingsAPIView.as_view()),
    ]