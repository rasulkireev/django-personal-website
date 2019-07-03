from django.db import models
from tinymce import models as tinymce_models
from autoslug import AutoSlugField


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    description = tinymce_models.HTMLField()
    cover = models.ImageField(upload_to='project-images/')

    def __str__(self):
        return self.title
