from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer, TagSerializer, CommentSerializer, VoteSerializer
from .models import Post, Tag, Comment, Vote


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__id', 'author__username', 'tags__name', 'created_at', ]

    def get_object(self):
        id = self.kwargs.get('pk')
        if self.request.method in SAFE_METHODS:
            return get_object_or_404(Post, id=id)
        else:
            return get_object_or_404(Post, id=id, author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]

    def get_object(self):
        id = self.kwargs.get('pk')
        post_id = self.kwargs.get('post_pk')
        if self.request.method in SAFE_METHODS:
            return get_object_or_404(Comment, id=id, post_id=post_id)
        else:
            return get_object_or_404(Comment, id=id, post_id=post_id, author=self.request.user)

    def perform_create(self, serializer, **kwargs):
        post_id = self.kwargs.get('post_pk')
        serializer.save(author=self.request.user, post_id=post_id)


class TagView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class VoteView(ModelViewSet):
    queryset = Vote.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = VoteSerializer

    def perform_create(self, serializer, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get('post_pk'))
        choice = self.request.data['choice']
        post_user_vote = post.votes.filter(author=self.request.user).first()
        if post_user_vote and post_user_vote.choice == choice:
            post_user_vote.delete()
            return
        elif post_user_vote:
            post_user_vote.delete()
        vote = serializer.save(author=self.request.user, choice=choice)
        post.votes.add(vote)


