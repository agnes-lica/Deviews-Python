from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Tech


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        ...

    def create(self, validated_data: dict) -> Tech:
        ...
