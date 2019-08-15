from django.db import models
from django.contrib import admin
from .models import Idea
from martor.widgets import AdminMartorWidget


class IdeasAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Idea, IdeasAdmin)
