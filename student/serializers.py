from rest_framework import serializers
from .models import Student
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class StudentAddProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, data):
        try:
            validate_email(data['email'])
        except ValidationError:
            raise serializers.ValidationError("Invalid Email Format")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Passwords must have at least 8 characters")

