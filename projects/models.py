from django.db import models


class Post(models.Model):
    title = models.TextField()
    description = models.TextField()
    cover = models.ImageField(upload_to='project-images/')

    def __str__(self):
        return self.title
