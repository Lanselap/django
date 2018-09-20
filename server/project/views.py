from django.shortcuts import render

def project_catalog(request):

    return render(request, 'project/catalog.html', {})


def project_product(request):

    return render(request, 'project/product.html', {})


def project_index(request):

    return render(request, 'project/index.html', {})    
