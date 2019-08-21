from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    draft = models.BooleanField(default = False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    buylink = models.URLField(max_length=200, blank=True)
    slug = AutoSlugField(populate_from='title', unique_with='title', editable=True)
    date_read = models.DateField()
    description = models.TextField(blank=True)
    rank = models.IntegerField(blank=True, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)])
    cover = models.ImageField(upload_to='book-cover/')

    def __str__(self):
        return self.title + " (Draft = " + str(self.draft) + ")"

class Book_toRead(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    buylink = models.URLField(max_length=200, blank=True)
    slug = AutoSlugField(populate_from='title', unique_with='title', editable=True)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='book-cover/')

    def __str__(self):
        return self.title + " (Draft = " + str(self.draft) + ")"
