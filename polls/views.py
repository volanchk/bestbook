import matplotlib.pyplot as plt
from django.shortcuts import render, redirect, reverse
from .forms import BooksForm, TopicsForm
from .models import Topics, Books
from matplotlib.figure import Figure


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

    topic_name = Topics.objects.get(id=pk)
    books = [i['name'] for i in Books.objects.values('name').filter(topic=pk)]
    score = [i['votes'] for i in Books.objects.values('votes').filter(topic=pk)]

    plt.style.use('Solarize_Light2')
    fig = Figure()
    ax = fig.subplots()
    votes = ax.bar(books, score, color="coral",
                   width=0.1, align="center",
                   edgecolor="black", linewidth=0,
                   label=topic_name)
    ax.bar_label(votes)
    ax.set_title(f'{topic_name}')
    plot = f"static/scores/{topic_name}.png"

    fig.savefig(plot)

    picture_existence = bool

    try:
        picture_existence = open(plot, 'r')

    except FileNotFoundError:

        picture_existence = False

    finally:

        print(picture_existence)

    if request.POST.get('choice'):
        result = request.POST.get('choice')
        entry = Books.objects.get(id=result)
        entry.votes += 1
        entry.save()
        return redirect('.')

    context = {
        "form": form,
        "topic": pk,
        "books_list": books_queryset,
        "pic": plot,
        "picture_state": picture_existence
    }

    return render(request, "election.html", context)
