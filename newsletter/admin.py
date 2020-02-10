from django.db import models
from django.contrib import admin
from .models import Email
from martor.widgets import AdminMartorWidget

class NewsletterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Email, NewsletterAdmin)