from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .permissions import IsAuthorEditObjectOrReadOnly
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework import viewsets, status
from rest_framework.decorators import action

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorEditObjectOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        """This works better than queryset because queryset has cache."""
        return Post.objects.filter(status=True)

    @action(methods=['get'], detail=False)
    def get_myposts(self, request):
        myposts = Post.objects.filter(status=True).filter(author__user=self.request.user)
        serializer = PostSerializer(myposts, many=True)
        return Response(serializer.data)



class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer

    def get_queryset(self):
        """This works better than queryset because queryset hs cache."""
        return Category.objects.all()