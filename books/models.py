from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    buylink = models.URLField(max_length=200, blank=True)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    description = models.TextField(blank=True)
    rank = models.IntegerField(blank=True, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)])
    cover = models.ImageField(upload_to='book-cover/', blank=True)

    completed = 'Completed'
    in_progress = 'Currently Reading'
    to_read = 'To Read'
    pause = 'Pause'

    status = [
        (completed, 'Completed'),
        (in_progress, 'Currently Reading'),
        (to_read, 'To Read'),
        (pause, 'Pause'),
    ]
    status = models.CharField(
        max_length=20,
        choices=status,
        default=to_read,
    )

    def __str__(self):
        return self.title
