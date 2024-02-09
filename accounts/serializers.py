from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        show_password = self.context.get("show_password", False)
        if not show_password:
            data.pop("password", None)
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password)
        return super().create(validated_data)
