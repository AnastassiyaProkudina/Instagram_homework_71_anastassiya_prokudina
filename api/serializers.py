from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(default=0, read_only=True, source='comments.count')

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'author', 'created_at', 'updated_at', 'comments_count']
        read_only_fields = ['id', 'author', 'created_ad', 'updates_at', 'comments_count']

    def create(self, validated_data, author=None):
        return Post.objects.create(**validated_data, author=self.author)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text')
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class PostSUpdateSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(default=0, read_only=True, source='comments.count')

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'author', 'created_at', 'updated_at', 'comments_count']
        read_only_fields = ['id', 'image', 'author',  'created_ad', 'updates_at', 'comments_count']

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text')
        instance.save()
        return instance
