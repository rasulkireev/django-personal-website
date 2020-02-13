from django.db import models
from django.contrib import admin
from .models import Post, Book
from martor.widgets import AdminMartorWidget

class WritingsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Post, WritingsAdmin)
admin.site.register(Book, WritingsAdmin)

