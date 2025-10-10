from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Логін"
    )
    first_name = forms.CharField(
        label="Ім'я",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Призвіще",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        max_length=250,
        widget = forms.EmailInput(attrs={"class": "form-control"}),
        label="Електрона пошта"
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        max_length=100
    )
    password2 = forms.CharField(
        label="Повторіть пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        max_length=100
    )


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}), label="Логін")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Пароль")
