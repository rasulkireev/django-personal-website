from django.db import models
from autoslug import AutoSlugField


class Wiltw(models.Model):
    title = models.DateField()
    slug = AutoSlugField(populate_from='title', unique_with='title')
    draft = models.BooleanField(default = False)
    body = models.TextField()

    def __str__(self):
        return str(self.title) + " (Draft = " + str(self.draft) + ")"
