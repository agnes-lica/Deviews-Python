from rest_framework import serializers
from .models import FirePost, FireComments

class FirePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirePost
        fields = ["id", "user_id", "post_id", "exists"]
        read_only_fields = ["id", "user_id", "post_id", "exists"]

    def create(self, validated_data):
        fire = FirePost.objects.get_or_create(**validated_data)

        if not fire[1]:
            fire[0].delete()
            fire[0].exists = False

        return fire[0]

class FireCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireComments
        fields = ["id", "user_id", "comment_id", "exists"]
        read_only_fields = ["id", "user_id", "comment_id", "exists"]

    def create(self, validated_data):
        fire = FireComments.objects.get_or_create(**validated_data)

        if not fire[1]:
            fire[0].delete()
            fire[0].exists = False

        return fire[0]
        