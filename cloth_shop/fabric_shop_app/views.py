from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *

menu = [
    {'title': 'Для верхней одежды', 'url_name': 'true_cloth'},
    {'title': 'Подклады', 'url_name': 'lining'},
    {'title': 'Прочее', 'url_name': 'other'},
]


def main_view(request):
    cards = Cloth.objects.all()
    context = {
        'cards': cards,
        'menu': menu,
        'cat_selected': 0,
    }
    return render(request, 'fabric_shop_app/base.html', context=context)


def show_category(request, cat_id):
    cards = Cloth.objects.filter(cat_id=cat_id)

    if len(cards) == 0:
        return render(request, 'fabric_shop_app/not_found.html')

    context = {
        'cards': cards,
        'menu': menu,
        'cat_selected': cat_id,
    }
    return render(request, 'fabric_shop_app/base.html', context=context)


def show_card(request, card_id):
    card = get_object_or_404(Cloth, pk=card_id)

    context = {
        'card': card,
        'menu': menu,
        'name': card.name,
        'cat_selected': card.cat_id,
    }
    return render(request, 'fabric_shop_app/product_card.html', context=context)




