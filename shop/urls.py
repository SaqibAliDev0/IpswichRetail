# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # URL for product list
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # URL for product details
]
