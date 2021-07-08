from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer, TagSerializer, CommentSerializer
from .models import Post, Tag, Comment


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__id', 'author__username', 'tags__name', 'created_at', ]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Post, id=id, author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_object(self):
        id = self.kwargs.get('pk')
        post_id = self.kwargs.get('post_pk')
        return get_object_or_404(Comment, id=id, post_id=post_id, author=self.request.user)

    def perform_create(self, serializer, **kwargs):
        post_id = self.kwargs.get('post_pk')
        serializer.save(author=self.request.user, post_id=post_id)


class TagView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]