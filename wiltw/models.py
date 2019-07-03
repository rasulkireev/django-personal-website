from django.db import models
from autoslug import AutoSlugField


class Wiltw(models.Model):
    title = models.DateField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    body = models.TextField()

    def __str__(self):
        return str(self.title)
