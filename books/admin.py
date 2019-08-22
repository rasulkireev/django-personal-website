from django.db import models
from django.contrib import admin
from .models import Book
from martor.widgets import AdminMartorWidget

class BooksAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Book, BooksAdmin)
# admin.site.register(Book_toRead, BooksAdmin)
