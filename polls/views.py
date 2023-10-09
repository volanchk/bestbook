from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreation


# Create your views here.
def create_book(request):

    form = BookCreation(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form,
    }

    return render(request, 'add_book.html', context)
