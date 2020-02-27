from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages

import requests

from .models import Email
from .forms import NewsletterSignupForm


class NewsletterView(SuccessMessageMixin, CreateView):
    form_class = NewsletterSignupForm
    model = Email
    success_message = "Thanks for signing up>>>>>>"

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        self.object = form.save()
        
        emailoctopus_api_key = settings.EMAILOCTOPUS_API
        list_id = settings.OCTO_LIST_ID

        data = {
            "api_key": emailoctopus_api_key,
            "email_address": self.object.user_email
        }

        response = requests.post(f"https://emailoctopus.com/api/1.5/lists/{list_id}/contacts", data=data)

        response.status_code

        messages.success(self.request, 'Thanks for signing up<<<<')
        
        return HttpResponseRedirect(self.get_success_url())

