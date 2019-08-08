from django.db import models
from autoslug import AutoSlugField


class Photo(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    cover = models.ImageField(upload_to='gallery/')
    id_number = models.IntegerField(blank=True)

    def __str__(self):
        return self.title
