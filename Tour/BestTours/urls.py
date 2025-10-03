from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_tour/", views.add_tour, name="add tour"),
    path("add_reserv/", views.add_reserv, name="add reserv"),
]