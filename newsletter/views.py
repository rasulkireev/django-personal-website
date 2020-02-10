from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Email
from .forms import NewsletterSignupForm
from django.urls import reverse_lazy


class NewsletterHomeView(SuccessMessageMixin, CreateView):
    template_name = "newsletter/newsletter-home.html"
    form_class = NewsletterSignupForm
    model = Email
    success_url = reverse_lazy('home')
    success_message = "Thanks for signing up!"
    

