from django.shortcuts import render


def login(request):
    context = {
        'title': 'Mebelville - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Mebelville - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Mebelville - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...
