from django.contrib.auth import authenticate, get_user_model
from django import forms

User = get_user_model()


class SignUserIn(forms.BaseForm):
    pass


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user_password"
            }
        )
    )
    password2 = forms.CharField(
        label="Confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password_confirmation"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Create another name, please!")
        return username
