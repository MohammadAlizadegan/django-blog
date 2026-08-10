from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from ...models import Post
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PostList(ListCreateAPIView):
    """Retrieves post list and creates new post instance."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class PostDetail(RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a post instance."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

