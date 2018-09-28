from django.urls import path

from . import views

app_name = 'project'

urlpatterns = [
    path('catalog/', views.project_catalog, name='catalog'),
    path('product/', views.project_product, name='product'),
    path('', views.project_index, name='index'),
]
