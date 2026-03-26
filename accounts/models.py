from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('blog_list')