from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse

# Create your views here.


def landing_view(request):
    return render(request, 'landing/index.html', {})


@login_required
def home(request):
    return render(request, 'base.html', {})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('home'))
    else:
        return redirect(reverse('landing'))


def logout_view(request):
    logout(request)
    return redirect(reverse('landing'))