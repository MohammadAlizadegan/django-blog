from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status


class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        """This works better than queryset because queryset hs cache."""
        return Post.objects.filter(status=True)

    def list(self, request):
        """Return a list of all posts."""
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        """Return a specific post in post-list view with 'get' key."""
        post = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def create(self, request):
        """Create a new post in post-list view with 'post' key."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def update(self, request, pk=None):
        """Update an existing post in post-detail view with 'put' key."""
        post = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        """Delete an existing post in post-detail view with 'delete' key."""
        post = get_object_or_404(self.get_queryset(), pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)