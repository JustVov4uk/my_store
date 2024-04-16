from django.shortcuts import render


def catalog(request):
    context: dict[str, str] = {
        'title': 'Deluxe - Каталог',
        'goods': [
            {'image': 'deps/images/goods/samsungRB.jpg',
             'name': 'Холодильник SAMSUNG RB33J3',
             'description': "Двокамерний холодильник, об'ємом 350л, система розморожування суха, клас енергоспоживання А++.",
             'price': 150.00},

            {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
             'name': 'Холодильник BOSCH KGN39',
             'description': "Двокамерний холодильник, об'ємом 400л, система розморожування суха, клас енергоспоживання А++.",
             'price': 140.00},

            {'image': 'deps/images/goods/double bed.jpg',
             'name': 'Мікрохвильова піч Whirlpool MWP 101SB',
             'description': "Об'єм 20л, максимальна потужність 700Вт, спосіб приготування: мікрохвилі.",
             'price': 60.00},

            {'image': 'deps/images/goods/kitchen table.jpg',
             'name': 'Мікрохвильова піч GORENJE MO17E1',
             'description': "Об'єм 17л, максимальна потужність 700Вт, спосіб приготування: мікрохвилі.",
             'price': 65.00},

            {'image': 'deps/images/goods/kitchen table 2.jpg',
             'name': 'Прасувальна система TEFAL IXEO POWER QT2020',
             'description': 'Паровий удар, г/хв:200, 3 режими, подача пари до 90 г/хв.',
             'price': 70.00},

            {'image': 'deps/images/goods/corner sofa.jpg',
             'name': 'Прасувальна система PHILIPS All-In-One 8500',
             'description': 'Паровий удар, г/хв:300, 3 режими, подача пари до 90 г/хв.',
             'price': 60.00},

            {'image': 'deps/images/goods/bedside table.jpg',
             'name': 'Кавомашина PHILIPS Series 5400',
             'description': '12 видів кавових напоїв, молочна система LatteGo, 4 профілі користувача.',
             'price': 55.00},

            {'image': 'deps/images/goods/sofa.jpg',
             'name': 'Кавомашина KRUPS Essential',
             'description': '10 видів кавових напоїв, 3 режими температури, 3 ступені мелення кави.',
             'price': 90.00},

            {'image': 'deps/images/goods/office chair.jpg',
             'name': 'Пральна машина Bosch WAN28262',
             'description': 'Кількість програм: 16, клас енергоспоживання: А+++, максимальне завантаження: 8 кг.',
             'price': 130.00},

            {'image': 'deps/images/goods/plants.jpg',
             'name': 'Пральна машина INDESIT OMTWSE 61051',
             'description': 'Кількість програм: 16, клас енергоспоживання: А+++, максимальне завантаження: 6 кг.',
             'price': 150.00},

            {'image': 'deps/images/goods/flower.jpg',
             'name': 'Робот-пилосос Rowenta X-PLORER',
             'description': 'Тип прибирання: сухе та вологе, тип фільтра: HEPA, рівень шуму, дБ: 65.',
             'price': 45.00},

            {'image': 'deps/images/goods/strange table.jpg',
             'name': 'Робот-пилосос Xiaomi Robot Vacuum S10+',
             'description': 'Тип прибирання: сухе та вологе, тип фільтра: HEPA, рівень шуму, дБ: 55.',
             'price': 35.00,
             },
        ],
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
