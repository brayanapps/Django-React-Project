from django.contrib.auth.models import UserAttributeSimilarityValidator
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"passowrd": {"write_only": True}}

        def create(self, validate_data):
            user = User.objects.create_user(**validated_data)
            return user
            