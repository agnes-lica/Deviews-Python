from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = [
            "id",
            "name",
            "username",
            "password",
            "email",
            "bio",
            "profile_picture",
            "is_active",
            "is_superuser",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["is_active"]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        User.objects.all(), "A user with that username already exists."
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(User.objects.all(), "This field must be unique.")
                ]
            },
        }

    def create(self, validated_data):
        print(validated_data)
        if validated_data.get("is_superuser"):
            user = User.objects.create_superuser(**validated_data)
            return user
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if not key == "is_superuser":
                setattr(instance, key, value)

        instance.save()

        return instance


class UserListSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ["id", "name", "bio", "profile_picture"]


class UserIsActiveSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = [
            "id",
            "name",
            "username",
            "password",
            "email",
            "bio",
            "profile_picture",
            "is_superuser",
            "created_at",
            "updated_at",
            "is_active",
        ]
        read_only_fields = [
            "id",
            "name",
            "username",
            "password",
            "email",
            "bio",
            "profile_picture",
            "is_superuser",
            "created_at",
            "updated_at",
        ]
