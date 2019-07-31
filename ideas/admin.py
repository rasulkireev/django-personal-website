from django.contrib import admin
from .models import Idea
from django_summernote.admin import SummernoteModelAdmin

class IdeasAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Idea, IdeasAdmin)
