from django.db import models
from autoslug import AutoSlugField


class Project(models.Model):
    title = models.CharField(max_length=200)
    homeurl = models.URLField(max_length=200, blank=True)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='project-images/', blank=True)

    Project = 'Project'
    Hustle = 'Hustle'
    PROJECT_TYPE = [
        (Project, 'Project'),
        (Hustle, 'Hustle'),
    ]
    project_type = models.CharField(
        max_length=10,
        choices=PROJECT_TYPE,
        default=Project,
    )

    def __str__(self):
        return self.title
