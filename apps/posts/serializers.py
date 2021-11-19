from rest_framework import serializers

from apps.users.models import UserProfile
from .models import Post, Comment, Tag, Vote


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = UserProfile


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'author')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = AuthorSerializer(instance.author).data
        return representation


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())
    comments = serializers.SerializerMethodField('get_comments')

    class Meta:
        model = Post
        fields = '__all__'

    def get_comments(self, instance):
        comments = Comment.objects.filter(post=instance.id)
        serializer = CommentSerializer(instance=comments, many=True)
        return serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = AuthorSerializer(instance.author).data
        return representation


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
