from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        ...

    def create(self, validated_data: dict) -> Comment:
        ...
