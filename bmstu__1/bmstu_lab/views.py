from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from datetime import date

products_list = [
    {
        'id': 1,
        'company': 'ОАО «Вертолёты России»',
        'product': 'Вертолеты',

    },
    {
        'id': 2,
        'company': 'ОАО «АХК „Сухой“»',
        'product': 'Самолеты',},
    {
        'id': 3,
        'company': 'ОАО «Курганский машиностроительный завод»',
        'product': 'Бронетехники',},
]

productss_list = [
    {
        'id': 1,
        'name_product': 'МИ-38, '
                        'КА-52, '
                        'КА-50, '
                        'МИ-24 ',
    },
    {
        'id': 2,
        'name_product': 'СУ-57, '
                        'СУ-37 ',

    },

    {
        'id': 3,
        'name_product': 'БМП-2, '
                        'БТР-1, '
                        'БТР-2М ',
    }
]


def home(request):
    return redirect('products')


def products(request):
    return render(request, 'products.html', {
        'current_date': date.today().strftime('%d.%m.%y'),
        'products': products_list
    })


def view_products(request, id):
    company = next((company for company in products_list if company['id'] == id), None)
    product = next((product for product in productss_list if product['id'] == id), None)
    if company:
        return render(request, 'view_products.html', {
            'current_date': date.today().strftime('%d.%m.%y'),
            'company': company,
            'product': product,
        })
    else:
        return HttpResponseNotFound(f'Product with id {id} not found')
