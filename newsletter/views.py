from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Email
from .forms import NewsletterSignupForm


class NewsletterView(SuccessMessageMixin, CreateView):
    form_class = NewsletterSignupForm
    model = Email
    success_message = "Thanks for signing up!"

    def get_success_url(self):
        return self.request.path

