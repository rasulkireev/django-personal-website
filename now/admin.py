from django.db import models
from django.contrib import admin
from .models import Now
from martor.widgets import AdminMartorWidget

class NowAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Now, NowAdmin)
