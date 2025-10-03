from django import forms

from .models import Reserv, Tour


class TourForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Назва туру",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        max_length=200,
        label="Опис туру",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Ціна",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

class ReservForm(forms.Form):
    tour = forms.ModelChoiceField(
        queryset=Tour.objects.all(),
        label="Тур",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    name = forms.CharField(
        max_length=100,
        label="Ім'я",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    