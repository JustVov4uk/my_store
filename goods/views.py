from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from goods.models import Products


def catalog(request, category_slug, page=1):
    if category_slug == 'all-goods':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context: dict[str, str] = {
        'title': 'Deluxe - Каталог',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):

    product: Products = Products.objects.get(slug=product_slug)

    context: dict[str, Products] = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)
