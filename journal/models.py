from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator


class Journal(models.Model):
    date = models.DateField()
    topic = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.date
