from django.db import models
from django.contrib import admin
from .models import Wiltw
from martor.widgets import AdminMartorWidget

class WiltwAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Wiltw, WiltwAdmin)
