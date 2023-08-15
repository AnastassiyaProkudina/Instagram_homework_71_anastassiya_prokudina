from rest_framework import serializers

from accounts.models import Account
from posts.models import Post, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(default=0, read_only=True, source='comments.count')
    likes_count = serializers.IntegerField(default=0, read_only=True, source='likes.count')

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'author', 'created_at', 'updated_at', 'comments_count', 'likes_count']
        read_only_fields = ['id', 'author', 'created_ad', 'updates_at', 'comments_count', 'likes_count']

    def create(self, validated_data, author=None):
        return Post.objects.create(**validated_data, author=self.author)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text')
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'email')
        read_only_fields = ('email',)


class LikeSerializer(serializers.ModelSerializer):
    post_text = serializers.CharField(read_only=True, source='post.text')
    post_image = serializers.ImageField(read_only=True, source='post.image')
    author = AccountSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'author', 'post', 'post_text', 'post_image')
        read_only_fields = ('id', 'author', 'post_text', 'post_image')

    def create(self, validated_data, account=None):
        return Like.objects.create(**validated_data, author=self.author)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_ad', 'updates_at', 'comments_count']

    def create(self, validated_data, author=None):
        comment = Comment.objects.create(**validated_data, author=self.author)
        return comment
