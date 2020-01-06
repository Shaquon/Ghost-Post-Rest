from ghost.models import Post
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'is_boast',
            'content',
            'upvotes',
            'downvotes',
            'submit_time'
        ]

