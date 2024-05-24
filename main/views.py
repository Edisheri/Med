from django.http import HttpResponse
from django.shortcuts import render

from services.models import  Categories

def index(request):
    categories = Categories.objects.all()


    context = {
        'title': 'Главная страница',
        'content': 'Сайт медицинской диагностики - MedSite',
        'categories' : categories
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Тут мы рассказываем какие мы хорошие и как хорошо мы диагностируем пациентов'
    }
    return render(request, 'main/about.html', context)
