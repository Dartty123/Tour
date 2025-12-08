from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import SignUpForm, LoginForm, UserEdit, ProfileForm
from django.views.decorators.http import require_POST, require_GET

# Create your views here.

def sign_up(request):
    form = SignUpForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        Profile.objects.create(user=user)
        user.profile.save()
        login(request=request, user=user)
        messages.add_message(request=request, level=messages.SUCCESS, message="Вітаємо з реєстрацією!")
        return redirect("index")
    
    return render(request=request, template_name="sign_up.html", context=dict(form=form))


def sign_in(request):
    form = LoginForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )
        if user is not None:
            login(request=request, user=user)
            messages.add_message(request=request, level=messages.SUCCESS, message="Успішний вхід")
            return redirect("index")
            
    return render(request=request, template_name="login.html", context=dict(form=form))

@login_required(login_url="/sign_in/")
def index(request):
    return render(request=request, template_name="index_user.html")


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return redirect("sign_in")


@login_required
@require_GET
def profile_user(request: HttpRequest):
    form_user = UserEdit(data=request.POST or None, instance=request.user)
    form_profile = ProfileForm(instance=request.user)
    return render(request, "profile.html", dict(form_user=form_user, form_profile=form_profile))


@login_required
@require_POST
def update_profile_user(request: HttpRequest):
    form_user = UserEdit(data=request.POST or None, instance=request.user)
    form_profile = ProfileForm(data=request.POST or None, files=request.FILES or None, instance=request.user)

    if form_user.changed_data:
        form_user.save()

    if form_profile.changed_data:
        form_profile.save()

    messages.success(request, "Дані успішно оновлені")
    return redirect("profile_user")
