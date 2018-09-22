from django.urls import path

from . import views

urlpatterns = [
    path('catalog/', views.project_catalog),
    path('product/', views.project_product),
    path('', views.project_index),
]
