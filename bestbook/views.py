from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
# from .forms import RegisterForm


def home(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")


def log_in(request):
    return render(request, "login.html")


def log_out(request):
    logout(request)

    return render(request, "index.html")
