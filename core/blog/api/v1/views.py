from django.db.migrations import serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404



@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly]) #Everyone can see but can't create.
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data) #It is important data= (it is used in is_valid function)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    return None


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly]) #Everyone can see but can't edit and delete.
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        return Response(PostSerializer(post).data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"Item deleted successfullt"},status=status.HTTP_204_NO_CONTENT)