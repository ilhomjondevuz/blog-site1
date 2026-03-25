from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = 'blog'
urlpatterns = [
    path('blogs/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_edit'),
    path('blogs/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('blogs/new/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]