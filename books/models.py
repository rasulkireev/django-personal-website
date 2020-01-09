from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    statuses = [
        ('READ', 'READ'),
        ('TO READ', 'TO READ'),
        ('READING','READING'),
    ]
    
    title = models.CharField(max_length=200)
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
    
    slug = AutoSlugField(populate_from='title', unique_with='title', always_update=True)

    def __str__(self):
        return self.title + " (Status = " + str(self.status) + ")"

    def get_absolute_url(self):
        return reverse('book', args=[str(self.slug)])
