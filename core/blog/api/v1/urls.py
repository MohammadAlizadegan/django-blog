from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


urlpatterns = [
    path('post/', views.postList, name='post-list'),
]