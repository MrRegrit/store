

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store',

    }
    return render(request, 'products/index.html', context)


def products(request):
    contect = {
        'title': 'Store - Каталог',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'url': '/static/vendor/img/products/Adidas-hoodie.png',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'name': 'Синяя куртка The North Face',
                'url': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'price': 23725
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'url': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'price':  3390
            }
        ]

    }
    return render(request, 'products/products.html', contect)
