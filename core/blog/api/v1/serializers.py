from rest_framework import serializers
from unicodedata import category

from ...models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     status = serializers.BooleanField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    url = serializers.HyperlinkedIdentityField(view_name='blog:api-v1:post-detail', read_only=True)
    class Meta:
        model=Post
        fields = "__all__"
    def to_representation(self, instance): #to change something in showing. (Show the name and create by id)
        request = self.context.get('request')
        rep = super().to_representation(instance) #get all parameters to show
        #rep['category'] = CategorySerializer(instance.category).data #change 'category' parameter. instance is the post object.
        if request.parser_context.get('kwargs').get('pk'): #Access to post-detail page.
            rep.pop('snippet', None) #Delete 'snippet' from post-detail
            rep.pop('url', None) #Delete 'url' from post-detail
        else:
            rep.pop('content', None) #Delete 'content' from post-list
        return rep