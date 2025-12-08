from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index_user"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile_user, name="profile_user"),
    path("update_profile/", views.update_profile_user, name="update_profile"),
]