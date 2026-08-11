from rest_framework import serializers
from unicodedata import category

from ...models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     status = serializers.BooleanField()

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    url = serializers.HyperlinkedIdentityField(view_name='blog:api-v1:post-detail', read_only=True)
    category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())
    class Meta:
        model=Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"