from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls

# urlpatterns = [
#     path('post/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
#     #path('', include(router.urls)),
# ]
#urlpatterns += router.urls