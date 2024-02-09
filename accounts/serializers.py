from rest_framework import serializers
from rest_framework.fields import empty

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
