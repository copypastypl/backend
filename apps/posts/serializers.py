from rest_framework import serializers

from apps.users.models import UserProfile
from .models import Post, Comment, Tag


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = UserProfile


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = AuthorSerializer(instance.author).data
        return representation


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'