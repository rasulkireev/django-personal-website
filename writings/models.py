from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from taggit.managers import TaggableManager
from django.forms import ModelForm


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    slug = AutoSlugField(populate_from='title', unique_with='title', always_update=True)
    draft = models.BooleanField(default = False)
    body = models.TextField()
    cover = models.ImageField(upload_to='post-images/', blank=True)
    main_image = models.ImageField(upload_to='main-post-images/', blank=True)
    date = models.DateTimeField()
    tags = TaggableManager(blank=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return "(Draft = " + str(self.draft) + ") " + self.category + ': ' + self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])

class Comment(models.Model):
    post = models.ForeignKey('writings.Post', on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=200)
    author_email = models.EmailField(blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text