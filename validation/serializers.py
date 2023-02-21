from rest_framework import serializers
from .models import CustomUser, Profile
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True},
                        'password2': {'write_only': True}}

        def validate(self, data):
            try:
                validate_email(data['email'])
            except ValidationError:
                raise serializers.ValidationError("Invalid Email Format")
            if len(data['password']) < 8:
                raise serializers.ValidationError("Passwords must be at least 8 characters")
            if data['password'] != data['password2']:
                raise serializers.ValidationError("Passwords do not match")

            if CustomUser.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('User with given email already exists')
            return data

        def create(self, validated_data):
            user = CustomUser.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password']
            )
            return user
