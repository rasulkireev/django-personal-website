from mentions.models.mixins.mentionable import MentionableMixin
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from taggit.managers import TaggableManager
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator



class Post(MentionableMixin, models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    slug = models.SlugField()
    draft = models.BooleanField(default = False)
    body = models.TextField()
    cover = models.ImageField(upload_to='post-images/', blank=True)
    main_image = models.ImageField(upload_to='main-post-images/', blank=True)
    date = models.DateTimeField()
    tags = TaggableManager(blank=True)
    category = models.CharField(max_length=100)

    def all_text(self) -> str:
        return f'{self.title} {self.body}'
        
    def __str__(self):
        return "(Draft = " + str(self.draft) + ") " + self.category + ': ' + self.title

    def get_absolute_url(self) -> str:
        return reverse('post', kwargs={'slug': self.slug})

    @property
    def day_of_the_week(self):
        return self.date.strftime("%A")

    @property
    def day_of_the_month(self):
        return self.date.strftime("%d")
    
    @property
    def month(self):
        return self.date.strftime("%B")

    @property
    def year(self):
        return self.date.strftime("%Y")

    @property
    def word_count(self):
        return len(self.body.split())