from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Главная - Mebelville',
        'content': 'Магазин мебели Mebelville',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас - Mebelville',
        'content': 'О нас',
        'text_on_page': 'Текст о том, какой магазин классный и какой он хороший',
    }

    return render(request, 'main/about.html', context)

