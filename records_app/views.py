from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import LoginForm, CreateUserForm


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/dashboard')

    context = {'form': form}

    return render(request, "index.html", context)


def login(request):
    return render(request, "login.html")


def dashboard(request):
    return render(request, "dashboard.html")
