from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    draft = models.BooleanField(default = False)
    body = models.TextField()
    cover = models.ImageField(upload_to='post-images/', blank=True)
    date = models.DateTimeField()
    tags = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "(Draft = " + str(self.draft) + ")    " + self.category + ': ' + self.title

    def get_absolute_url(self):
        return reverse('writings.views.PostDetailView', args=[str(self.slug)])
