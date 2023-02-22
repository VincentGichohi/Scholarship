from operator import imod
from django.urls import path
from knox import views as knox_views
from .views import SignInAPIView, SignUpAPI, MainUser