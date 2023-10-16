from django.shortcuts import render, redirect, reverse
from .forms import BooksForm, TopicsForm
from .models import Topics, Books


def create_topic(request):

    form = TopicsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        "form": form,
    }

    return render(request, "add_topic.html", context)


def add_book(request, pk):

    form = BooksForm(request.POST or None)
    name = Topics.objects.get(pk=pk)

    if form.is_valid():
        form.save()
        return redirect(f"/{pk}/election")

    context = {
        "form": form,
        "topic": pk,
        "topic_name": name
    }

    return render(request, "add_book.html", context)


def election(request, pk):

    books_queryset = Books.objects.all().filter(topic=pk)

    form = BooksForm(request.POST or None)

    if request.POST.get('choice'):
        result = request.POST.get('choice')
        entry = Books.objects.get(id=result)
        entry.votes += 1
        entry.save()
        return redirect('/')

    context = {
        "form": form,
        "topic": pk,
        "books_list": books_queryset
    }

    return render(request, "election.html", context)
