from django.shortcuts import render

from .models import Category, Product

def project_catalog(request):

    product = Product.objects.all()[:8]

    context = {
        'product':product,
    }

    return render(request, 'project/catalog.html', context)


def project_product(request):

    context = {
        'results':[
           'Home',
           'Catalog',
        ]
    }

    return render(request, 'project/product.html', context)


def project_index(request):

    return render(request, 'project/index.html', {})    
