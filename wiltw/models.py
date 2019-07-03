from django.db import models
from tinymce import models as tinymce_models
from autoslug import AutoSlugField


class Wiltw(models.Model):
    title = models.DateField()
    slug = AutoSlugField(populate_from='title', unique_with='title')
    body = tinymce_models.HTMLField()

    def __str__(self):
        return str(self.title)
