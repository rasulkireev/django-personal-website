from rest_framework import serializers
from health.models import WeightMeasurement


class WeightSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeightMeasurement
        fields = ('date_and_time', 'weight')