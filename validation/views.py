from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = RegisterForm
    success_message = "Your user account has been created successfully"
