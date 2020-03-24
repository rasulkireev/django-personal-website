from rest_framework import generics
from writings.models import Post
from .serializers import WritingsSerializer


class WritingsAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(draft="False").order_by('date')
    serializer_class = WritingsSerializer