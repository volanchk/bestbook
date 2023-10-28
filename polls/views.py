import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from .forms import BooksForm, TopicsForm
from .models import Topics, Books, Votes
from matplotlib.figure import Figure


# The election function began to grow dangerously large,
# so I've decided to move plot creation in a separate function.
def create_plot(topic, titles, voices):
    plt.style.use('Solarize_Light2')
    fig = Figure()
    ax = fig.subplots()
    colors = ['#B33C86', '#51A3A3', '#EA638C']
    colors_2 = ['#34344A', '#80475E', '#CC5A71', '#C89B7B', '#F0F757']
    # '#51A3A3'
    votes = ax.bar(titles, voices, color='#80475E',
                   width=0.1, align="center",
                   edgecolor="black", linewidth=0,
                   label=topic)
    ax.bar_label(votes)
    ax.set_title(f'{topic}')
    path = f"static/scores/{topic}.png"

    fig.savefig(path)

    return path


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

    books_not_empty = Books.objects.filter(topic=pk).exists()
    books_queryset = Books.objects.all().filter(topic=pk)
    votes_not_empty = Votes.objects.filter(topic=pk).exists()

    voters = Votes.objects.values_list('user_id', flat=True).filter(topic=pk)

    form = BooksForm(request.POST or None)

    topic_name = Topics.objects.get(id=pk)

    books = [i['name'] for i in Books.objects.values('name').filter(topic=pk)]
    score = [i['votes'] for i in Books.objects.values('votes').filter(topic=pk)]

    plot = create_plot(topic_name, books, score)

    if request.POST.get('choice'):
        result = request.POST.get('choice')
        book_entry = Books.objects.get(id=result)
        book_entry.votes += 1
        vote_entry = Votes(topic=pk, user_id=request.user.id, book_id=book_entry.id)
        vote_entry.save()
        book_entry.save()
        return redirect('.')

    context = {
        "form": form,
        "topic": pk,
        "books_list": books_queryset,
        "pic": plot,
        "voters": voters,
        "books_not_empty": books_not_empty,
        "votes_not_empty": votes_not_empty,
        "name": topic_name
    }

    # print(books_not_empty)
    # print(votes_not_empty)

    return render(request, "election.html", context)


def un_vote(request, pk):
    vote_entry = Votes.objects.get(topic=pk, user_id=request.user.id)
    book_entry = Books.objects.get(id=vote_entry.book_id)
    vote_entry.delete()
    book_entry.votes -= 1
    book_entry.save()
    return redirect(f'/{pk}/election')
