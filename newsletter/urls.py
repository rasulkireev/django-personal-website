from django.urls import path
from .views import NewsletterHomeView

urlpatterns = [
        path('', NewsletterHomeView.as_view(), name='newsletter-home'),
            ]
