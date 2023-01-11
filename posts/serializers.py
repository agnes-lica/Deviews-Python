from rest_framework import serializers
from .models import Post
from users.serializers import UserSerializer
from techs.serializers import TechSerializer
from fires.serializers import FirePostSerializer
from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tech = TechSerializer(read_only=True)
    fires = FirePostSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "content", "post_picture", "created_at", "updated_at", "user", "tech", "fires", "comments"]
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data: dict) -> Post:
        return Post.objects.create(**validated_data)
