from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect
from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import CustomUser
from rest_framework import generics
from knox.models import AuthToken
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from knox.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions, serializers
from rest_framework import status
from django.template.response import TemplateResponse
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from rest_framework.views import APIView
# from rest_framework_social_oauth2.authentication import SocialAuthentication
from social_django.utils import psa

User = get_user_model()


class SignUpAPI(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        return Response({
            'user': RegisterSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })


class SignInAPI(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


class MainUser(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
