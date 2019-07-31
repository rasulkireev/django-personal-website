from django.contrib import admin
from .models import Journal
from django_summernote.admin import SummernoteModelAdmin

class JournalAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Journal, JournalAdmin)
