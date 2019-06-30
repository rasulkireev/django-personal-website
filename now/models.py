from django.db import models


class Post(models.Model):
    title = models.DateField(blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return str(self.title)
