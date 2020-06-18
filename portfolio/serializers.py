from rest_framework import serializers
from .models import ForumPost


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ('id',
                  'title',
                  'content',
                  'author'
                  )
