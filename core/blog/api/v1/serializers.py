from rest_framework import serializers
from ...models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     status = serializers.BooleanField()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ['id', 'title', 'author', 'content', 'created_at', 'published_at', 'status']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']