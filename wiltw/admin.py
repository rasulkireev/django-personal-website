from django.contrib import admin
from .models import Wiltw
from django_summernote.admin import SummernoteModelAdmin

class WiltwAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Wiltw, WiltwAdmin)
