from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories


def index(request) -> HttpResponse:
    categories = Categories.objects.all()
    context: dict[str, str] = {
        'title': 'Deluxe - Головна',
        'content': 'Магазин побутової техніки DELUXE',
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str, str] = {
        'title': 'Deluxe - Про нас',
        'content': 'Про нас',
        'text_on_page': """ Інтернет-магазин техніки підтримує співпрацю з усіма виробниками побутової техніки. 
                    Тому, у нас Ви знайдете усі необхідні товари саме тих виробників, які Вас цікавлять. 
                    У наш магазин постійно додаються товари нових популярних моделей та знижуються ціни на старіші.    
                    Ми розробили зручний для користування сайт нашого інтернет-магазину побутової техніки, щоб наші
                    покупці відразу змогли знайти потрібний товар на сайті, його опис, характеристику, ціну та замовити.
                    У нашому інтернет-магазині побутової техніки ми завжди проводимо різноманітні акції, знижки 
                    та розіграші популярних товарів. "
                    Тому, підписавшись на наші новини чи на соціальні мережі, Ви будете в курсі цих новинок."""
    }

    return render(request, 'main/about.html', context)
