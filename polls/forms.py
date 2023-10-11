from django import forms
from .models import Book, Topic


class CreateTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            "topic"
        ]


class BookCreation(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title"
        ]

