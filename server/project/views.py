from django.shortcuts import render

def project_catalog(request):

    return render(request, 'project/catalog.html', {})


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
