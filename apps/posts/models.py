from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=36)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.CharField(max_length=64)

    def get_tags(self):
        return self.tags.split(',')