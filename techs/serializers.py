from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Tech


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = ["id", "tech_name"]
        read_only_fields = ["id"]
        # extra_kwargs = {
        #     "tech_name": {
        #         "validators": [
        #             UniqueValidator(
        #                 Tech.objects.all(), "Tech already exists."
        #             )
        #         ]
        #     }
        # }

    def create(self, validated_data: dict) -> Tech:
        print("asnjf")
        return Tech.objects.create(**validated_data)

    def update(self, instance: Tech, validated_data: dict) -> Tech:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
