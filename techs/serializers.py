from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Tech


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ["id", "tech_name"]
        read_ondly_fields = ["id"]

    def create(self, validated_data: dict) -> Tech:
        return Tech.objects.create(**validated_data)

    def update(self, instance: Tech, validated_data: dict) -> Tech:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
