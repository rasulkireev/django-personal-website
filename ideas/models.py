from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator

class Idea(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, blank=True)
    working = models.BooleanField()
    description = models.TextField(blank=True)
    ease = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)])
    interest = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)])
    profit = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)])


    def __str__(self):
        return self.title
