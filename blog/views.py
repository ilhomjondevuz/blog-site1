from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/blog_create.html'
    fields = '__all__'
    # success_url = reverse_lazy('blog:blog_detail', kwargs={'pk': object.pk})

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/blog_edit.html'
    fields = ['title', 'content', 'photo']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:blog_list')