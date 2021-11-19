from django.db import models


class VoteChoice(models.TextChoices):
    UPVOTE = "upvote", "upvote"
    DOWNVOTE = "downvote", "downvote"


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)


class Vote(models.Model):
    author = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE, null=True)
    choice = models.CharField(choices=VoteChoice.choices, max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=36)
    content = models.TextField()
    author = models.ForeignKey("users.UserProfile", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    votes = models.ManyToManyField(Vote)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)