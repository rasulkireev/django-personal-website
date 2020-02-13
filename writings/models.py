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


class Book(models.Model):
    statuses = [
        ('READ', 'READ'),
        ('TO READ', 'TO READ'),
        ('READING','READING'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    author = models.CharField(max_length=200)
    date_read = models.DateField(blank=True, null=True)
    date_published = models.DateField(auto_now_add=True)
    cover = models.ImageField(upload_to='book-cover/', blank=True)
    status = models.CharField(
        max_length=100,
        choices=statuses,
        default='TO READ'
    )
    
    main_category = models.CharField(max_length=200, blank=True)
    buylink = models.URLField(max_length=200, blank=True) 
    description = models.TextField(blank=True)
    rank = models.IntegerField(blank=True, null=True, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)])
    

    def __str__(self):
        return self.title + " (Status = " + str(self.status) + ")"

    def get_absolute_url(self):
        return reverse('book', args=[str(self.slug)])
