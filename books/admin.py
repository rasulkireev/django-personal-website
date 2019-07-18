from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin

class BooksAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Book, BooksAdmin)
