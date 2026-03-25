from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='posts/%Y/%m')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})