from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ('author', 'photo', 'title', 'text', 'created_date', 'published_date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'text', 'created_date', 'approved_comment')
