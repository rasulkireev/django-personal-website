from django.db import models
from autoslug import AutoSlugField


class WeightMeasurement(models.Model):
    date_and_time = models.DateTimeField()
    weight = models.FloatField()

    def __str__(self):
        return str(self.date_and_time)

    def get_absolute_url(self):
        return reverse('health-weight')


class MuscleMeasurement(models.Model):
    date_and_time = models.DateTimeField()
    left_bicep = models.FloatField()
    right_bicep = models.FloatField()
    left_thigh = models.FloatField()
    right_thigh = models.FloatField()
    waist = models.FloatField()

    def __str__(self):
        return str(self.date_and_time)

    def get_absolute_url(self):
        return reverse('health-muscles')

class ExerciseMeasurement(models.Model):
    intensities = [
        ('Light', 'Light'),
        ('Medium', 'Medium'),
        ('High','High'),
    ]
    date_and_time = models.DateTimeField()
    intensity = models.CharField(
        max_length=100,
        choices=intensities,
        default='Medium')

    length = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return str(self.date_and_time)

    def get_absolute_url(self):
        return reverse('health-exercise')

class CalorieMeasurement(models.Model):
    date_and_time = models.DateTimeField()
    calories = models.IntegerField()

    def __str__(self):
        return str(self.date_and_time)

    def get_absolute_url(self):
        return reverse('health-calories')