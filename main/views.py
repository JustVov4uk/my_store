from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Головна сторінка магазину - HOME',
        'list': ['first', 'second', 'third'],
        'dict': {'first': 1},
        'is_authenticated': False
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse('About page')
