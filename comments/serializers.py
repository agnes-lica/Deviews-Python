from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "updated_at", "user_id", "post_id"]

        read_only_fields = ["id", "user_id", "post_id", "created_at", "updated_at"]

    def create(self, validated_data: dict) -> Comment:
        return Comment.objects.create(**validated_data)

    def update(self, instance: Comment, validated_data: dict) -> Comment:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
