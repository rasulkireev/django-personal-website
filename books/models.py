from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    statuses = [
        ('READ', 'READ'),
        ('TO READ', 'TO READ'),
        ('READING','READING'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_read = models.DateField()
    cover = models.ImageField(upload_to='book-cover/')
    status = models.CharField(
        max_length=100,
        choices=statuses,
        default='TO READ'
    )
    
    
    main_category = models.CharField(max_length=200, blank=True)
    buylink = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    rank = models.IntegerField(blank=True, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)])
    
    
    slug = AutoSlugField(populate_from='title', unique_with='title', always_update=True)

    def __str__(self):
        return self.title + " (Status = " + str(self.status) + ")"
