from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        ...

    def create(self, validated_data: dict) -> User:
        ...

    def update(self, instance: User, validated_data: dict) -> User:
        ...
