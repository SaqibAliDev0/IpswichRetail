# shop/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product  # Ensure this import is correct

def product_list(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Get a specific product by ID
    return render(request, 'shop/product_detail.html', {'product': product})
