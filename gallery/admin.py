from django.db import models
from django.contrib import admin
from .models import Photo
from martor.widgets import AdminMartorWidget

class GalleryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Photo, GalleryAdmin)
