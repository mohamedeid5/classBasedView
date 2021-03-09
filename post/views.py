from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, UpdateView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-created_at'
    #context_object_name = 'posts'

    
    def get_queryset(self):
        return Post.objects.filter(active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'mohamed eid' 
        return context
        
    
    

class PostDetail(DetailView):
    model = Post
    pk_url_kwarg = 'pk'
    context_object_name = 'post'
    

