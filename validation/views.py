from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin


# class SignUpView(SuccessMessageMixin, CreateView):
#     template_name = ''