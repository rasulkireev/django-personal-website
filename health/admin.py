from django.contrib import admin
from .models import WeightMeasurement, MuscleMeasurement, ExerciseMeasurement, CalorieMeasurement


admin.site.register(WeightMeasurement)
admin.site.register(MuscleMeasurement)
admin.site.register(ExerciseMeasurement)
admin.site.register(CalorieMeasurement)