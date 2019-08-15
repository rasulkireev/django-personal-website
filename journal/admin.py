from django.db import models
from django.contrib import admin
from .models import Journal
from martor.widgets import AdminMartorWidget

class JournalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Journal, JournalAdmin)
