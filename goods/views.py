from django.shortcuts import render
from goods.models import Products


def catalog(request):
    goods = Products.objects.all()
    context: dict[str, str] = {
        'title': 'Deluxe - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
