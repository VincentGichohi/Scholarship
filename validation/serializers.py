from rest_framework import serializers
from .models import CustomUser, Profile
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from knox.serializers import UserSerializer as KnoxUserSerializer
from knox.models import AuthToken


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'is_staff')
        extra_kwargs =  {'password': {'write_only': True}}


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
        extra_kwargs = ({'password': {'write_only': True}})


# class SponsorSerializer()
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

        def save(self, **kwargs):
            user = super().save(*kwargs)
            AuthToken.objects.create(user=user)
            return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = CustomUser.objects.filter(email=data['email'], user_type=data['user_type']).first()
        if user and user.check_password(data['password']) and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials for user type")

    def save(self, **kwargs):
        user = self.validated_data
        AuthToken.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
