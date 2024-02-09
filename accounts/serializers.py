from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from cipher_safe_api.validators import (
    validate_contact_number,
    validate_country_code,
    validate_email,
    validate_password,
    validate_person_name,
)

from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
        read_only_fields = ["email_verified", "contact_no_verified"]

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

    def validate(self, attrs):
        errors = {}

        if not validate_person_name(attrs.get("name", "")):
            errors["name"] = "Name does not meet the criteria."

        if not validate_password(attrs.get("password", "")):
            errors["password"] = "Your password does not meet the criteria."

        if not validate_email(attrs.get("email", "")):
            errors["email"] = "Enter a valid email address."

        if not validate_country_code(attrs.get("country_code", "")):
            errors["country_code"] = "Enter valid country code."

        if not validate_contact_number(attrs.get("contact_no", "")):
            errors["contact_no"] = "Enter valid contact number."

        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(attrs)
