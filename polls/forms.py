from django import forms
from .models import Topics, Books


class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = [
            "topic"
        ]


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'name',
            'topic'
        ]
