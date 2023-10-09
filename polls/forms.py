from django import forms
from .models import Book


class BookCreation(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title", "topic",
            "author", "publisher",
            "year"
        ]

