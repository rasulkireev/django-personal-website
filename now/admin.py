from django.contrib import admin
from .models import Now
from django_summernote.admin import SummernoteModelAdmin

class NowAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Now, NowAdmin)
