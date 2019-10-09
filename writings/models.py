from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='title', always_update=True)
    draft = models.BooleanField(default = False)
    body = models.TextField()
    cover = models.ImageField(upload_to='post-images/', blank=True)
    date = models.DateTimeField()
    tags = models.CharField(max_length=200, blank=True)

    Coding = 'Coding'
    Cooking = 'Cooking'
    Personal = "Personal"
    POST_TYPE = [
        (Coding, 'Coding'),
        (Cooking, 'Cooking'),
        (Personal, 'Personal'),
    ]
    category = models.CharField(
        max_length=20,
        choices=POST_TYPE,
        default=Personal,
    )

    def __str__(self):
        return "(Draft = " + str(self.draft) + ") " + self.category + ': ' + self.title

    def get_absolute_url(self):
        return reverse('writings.views.PostDetailView', args=[str(self.slug)])
