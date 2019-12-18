from rest_framework import generics
from health.models import WeightMeasurement
from .serializers import WeightSerializer


class WeightAPIView(generics.ListAPIView):
    queryset = WeightMeasurement.objects.all()
    serializer_class = WeightSerializer