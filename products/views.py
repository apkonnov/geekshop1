from django.shortcuts import render
from django.conf import settings
import json


# Create your views here.


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    with open(settings.BASE_DIR / 'products/fixtures/products.json', 'r', encoding='utf-8') as f:
        product_list = json.load(f)

    context = {'title': 'GeekShop - Продукты',
               'products': product_list}
    return render(request, 'products/products.html', context)
