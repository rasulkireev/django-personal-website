from django.db import models
from django.contrib import admin
from .models import Project
from martor.widgets import AdminMartorWidget

class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Project, ProjectAdmin)
