from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'excerpt', 'content', 'status']
        read_only_fields = ['author']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        
        return super().create(validated_data)