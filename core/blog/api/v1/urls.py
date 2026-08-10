from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
]