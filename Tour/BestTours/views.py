from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import ReservForm, TourForm
from .models import Reserv, Tour
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request: HttpRequest):
    tour = Tour.objects.filter(tour=request.title).all()
    return render(request=request, template_name='index.html',tour=tour)

@login_required(login_url="/user/sign_in/")
def add_tour(request):
    form = TourForm()
    if request.method == "POST":
        form = TourForm(request.POST)
        if form.is_valid():
            tour=Tour(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price']
            )
            tour.save()
            return redirect('index')
    return render(request=request, template_name='add_tour.html', context=dict(form=form))


def add_reserv(request):
    form = ReservForm()
    if request.method == "POST":
        form = ReservForm(request.POST)
        if form.is_valid():
            reserv=Reserv(
                tour=form.cleaned_data['tour'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            reserv.save()
            return redirect('index')
    return render(request=request, template_name='add_reserv.html', context=dict(form=form))