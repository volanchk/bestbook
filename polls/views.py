import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from .forms import BooksForm, TopicsForm
from .models import Topics, Books
from matplotlib.figure import Figure
from random import choice


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
    colors = ['#B33C86', '#51A3A3', '#EA638C']
    colors_2 = ['#34344A', '#80475E', '#CC5A71', '#C89B7B', '#F0F757']
    # '#51A3A3'
    votes = ax.bar(books, score, color='#80475E',
                   width=0.1, align="center",
                   edgecolor="black", linewidth=0,
                   label=topic_name)
    ax.bar_label(votes)
    ax.set_title(f'{topic_name}')
    plot = f"static/scores/{topic_name}.png"

    fig.savefig(plot)

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
        "pic": plot
    }

    return render(request, "election.html", context)
