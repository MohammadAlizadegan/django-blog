from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.utils import timezone
from django.views.generic.edit import CreateView


class IndexView(TemplateView):
    """Shows index.html with CBV"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'AAA'
        context['posts'] = Post.objects.all()
        return context

class RedirectToGoogle(RedirectView):
    url = 'https://google.com'

class PostList(ListView):
    #model = Post
    context_object_name = 'posts'
    def get_queryset(self):
        query = Post.objects.filter(status=True)
        return query

    #paginate_by = 3

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostCreateView(CreateView):
    model = Post
    fields = ['author', 'title', 'content', 'status', 'category', 'published_at']
    success_url = '/blog/post/'