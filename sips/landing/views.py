from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse

# Create your views here.
from utils.constants import AGENTE_SOCIAL, DIRECTIVO, RECEPCION, TITULAR


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
        if user.groups.filter(name__in=[AGENTE_SOCIAL]):
            return redirect('listado_asuntos')
        elif user.groups.filter(name__in=[DIRECTIVO]):
            return redirect('listado_asuntos')
        elif user.groups.filter(name__in=[RECEPCION]):
            return redirect('listado_asuntos')
        elif user.groups.filter(name__in=[TITULAR]):
            return redirect('listado_asuntos')
        return redirect(reverse('home'))
    else:
        return redirect(reverse('landing'))


def logout_view(request):
    logout(request)
    return redirect(reverse('landing'))