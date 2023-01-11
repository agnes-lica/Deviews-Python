from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Comment
from users.serializers import UserSerializer
from fires.serializers import FireCommentSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    fires = FireCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "updated_at", "user", "fires"]

        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data: dict) -> Comment:
        return Comment.objects.create(**validated_data)

    def update(self, instance: Comment, validated_data: dict) -> Comment:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
