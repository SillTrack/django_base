from django.shortcuts import render

from mainapp.models import Product


def main(request):
    title = 'Магазин'

    products = Product.objects.all()[:]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context=context)

