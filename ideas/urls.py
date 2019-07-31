from django.urls import path
from .views import AllIdeas

urlpatterns = [
        path('', AllIdeas.as_view(), name='all_ideas'),
            ]
