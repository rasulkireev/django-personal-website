from django.urls import path
from .views import ProjectList

urlpatterns = [
    path('', ProjectList.as_view(), name='project_list'),
]
