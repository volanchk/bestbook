from django.contrib.auth import authenticate, get_user_model
from django import forms

User = get_user_model()


class SignUserIn(forms.BaseForm):
    pass


class RegisterForm(forms.Form):
    pass