from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import User
from .forms import RegisterForm, SignUserIn


def home(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login_fail')

    return render(request, "index.html")


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        try:
            User.objects.create_user(username=username,
                                     password=password)
        finally:
            user = None

        user = authenticate(request, username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

    return render(request, "register.html", {"form": form})


def log_in(request):

    form = SignUserIn(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

    return render(request, "login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("/")


def login_fail(request):
    return render(request, "login_fail.html")

