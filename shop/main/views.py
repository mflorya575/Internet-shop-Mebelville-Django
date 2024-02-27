from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'home',
        'content': 'Главная страница магазина - HOME',
        "list": [0, 1, 2],
        'dict': {'first': 1},
        'bool': True,
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')

