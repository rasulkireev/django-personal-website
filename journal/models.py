from django.db import models
from autoslug import AutoSlugField

class Journal(models.Model):
    date = models.DateField()
    topic = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return str(self.date) + ': ' + self.topic
