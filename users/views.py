from django.shortcuts import render
from users.forms import UserLoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Deluxe - Авторизація',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Deluxe - Реєстрація'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'Deluxe - Кабінет'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...