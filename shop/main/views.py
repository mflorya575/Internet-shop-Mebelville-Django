from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {
        'title': 'Главная - Mebelville',
        'content': 'Магазин мебели Mebelville',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас - Mebelville',
        'content': 'О нас',
        'text_on_page': 'Текст о том, какой магазин классный и какой он хороший',
    }

    return render(request, 'main/about.html', context)


def contact(request):
    context = {
        'title': 'Контактная информация - Mebelville',
        'content': 'Контактная информация',
        'address': '5171 В. Кэмпбел Авенью, США',
        'call_us': '(+91) - 540-025-124553',
        'email': 'mebelville@gmail.com',
        'hours': '10:00 - 18:00, Пн - Сб',
    }

    return render(request, 'main/contact.html', context)


def privacy_policy(request):
    context = {
        'title': 'Политика конфиденциальности - Mebelville',
        'content': 'Политика конфиденциальности',
        'text_on_page': 'Скоро здесь будет текст политики конфиденциальности',
    }

    return render(request, 'main/privacy-policy.html', context)

