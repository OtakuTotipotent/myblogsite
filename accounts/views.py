from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User


def signup_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("signup")

        user = User.objects.create_user(
            email=email,
            password=password,
            name=name,
        )
        login(request, user)
        return redirect(request, "home")
    return render(request, "accounts/signup.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(
            request,
            email=email,
            password=password,
        )
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "invalid email or password")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
