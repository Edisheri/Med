
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404

from services.models import Services
from services.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    one_sale = request.GET.get('one_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        services = Services.objects.all()
    elif query:
        services = q_search(query)

    else:
        services = get_list_or_404(Services.objects.filter(category__slug=category_slug))

    if one_sale:
        services = services.filter(discount__gt=0)
    if order_by and order_by != 'default':
        services = services.order_by(order_by)


    paginator = Paginator(services, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Услуги лабораторных исследований',
        'services': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'services/catalog.html', context)

def product(request, product_slug):
    product = Services.objects.get(slug=product_slug)
    context = {
     'product': product,
    }
    return render(request, 'services/product.html', context=context)
