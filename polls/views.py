from django.shortcuts import render, redirect, reverse
from .forms import BookCreation, CreateTopic


def create_topic(request):

    form = CreateTopic(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_book')

    context = {
        "form": form,
    }

    return render(request, 'add_topic.html', context)


def create_book(request):

    form = BookCreation(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form,
    }

    return render(request, 'add_book.html', context)
