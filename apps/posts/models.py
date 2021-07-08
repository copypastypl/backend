from django.db import models

from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=36)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)