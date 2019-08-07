from django.db import models
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    body = models.TextField()
    cover = models.ImageField(upload_to='post-images/', blank=True)
    date = models.DateTimeField()
    tags = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
