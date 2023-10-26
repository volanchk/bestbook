from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import User
from .forms import RegisterForm, SignUserIn
from polls.forms import TopicsForm, BooksForm
from polls.models import Topics, Books


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

    topics_queryset = Topics.objects.all()
    books_queryset = Books.objects.all()

    if request.GET or None:
        results = Topics.objects.filter(topic__contains=request.GET["q"])
        return render(request, "searching_results.html", {"results": results})

    context = {
        "topic_list": topics_queryset,
        "books_list": books_queryset
    }

    return render(request, "index.html", context)


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
