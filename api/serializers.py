from rest_framework import serializers
from writings.models import Post


class WritingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'date', 'category', 'description','body', 'word_count', 'day_of_the_week')