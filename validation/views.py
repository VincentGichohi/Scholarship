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

