from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('cbv-index/', views.IndexView.as_view(), name='cbv-index'),
    path('post/', views.PostList.as_view(), name = 'post-list'),
    path('google/', views.RedirectToGoogle.as_view(), name='google'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('create/', views.PostCreateView.as_view(), name='create')
]
