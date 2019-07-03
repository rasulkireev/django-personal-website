from django.db import models
from autoslug import AutoSlugField


class Project(models.Model):
    title = models.TextField()
    slug = AutoSlugField(populate_from='title', unique_with='title')
    description = models.TextField()
    cover = models.ImageField(upload_to='project-images/')

    def __str__(self):
        return self.title
