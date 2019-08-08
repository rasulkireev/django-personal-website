from django.contrib import admin
from .models import Photo
from django_summernote.admin import SummernoteModelAdmin

class GalleryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Photo, GalleryAdmin)
