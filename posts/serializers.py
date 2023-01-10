from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "content", "post_picture", "created_at", "updated_at", "user_id", "techs"]
        read_only_fields = ["created_at", "updated_at", "user_id", "techs"]

    def create(self, validated_data: dict) -> Post:
        return Post.objects.create(**validated_data)
