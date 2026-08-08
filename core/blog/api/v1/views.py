from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view()
def postList(request):
    return Response("OK!")

@api_view()
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id)
    return Response(PostSerializer(post).data)
    # try:
    #     post = Post.objects.get(pk=id)
    #     return Response(PostSerializer(post).data)
    # except Post.DoesNotExist:
    #     return Response({"detail":"object does not exist"}, status=status.HTTP_404_NOT_FOUND)