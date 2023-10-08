from django.contrib.auth import authenticate, get_user_model
from django import forms

User = get_user_model()


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "username"
        }
    ))

    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    password2 = forms.CharField(
        label="confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password-confirmation"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)

        if qs.exists():
            raise forms.ValidationError("Invalid name this is! Please create another!")
        return username


