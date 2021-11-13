from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.posts.models import Post


class UserProfile(AbstractUser):
    favourite_posts = models.ManyToManyField(Post)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return 'test'
