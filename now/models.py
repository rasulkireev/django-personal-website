from django.db import models
from autoslug import AutoSlugField


class Now(models.Model):
    title = models.DateField()
    slug = AutoSlugField(populate_from='title', unique_with='title')
    body = models.TextField()

    def __str__(self):
        return str(self.title)
