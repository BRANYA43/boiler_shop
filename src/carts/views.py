from django.http import HttpRequest
from django.shortcuts import redirect

from products.models import Product

from .cart import Cart


def cart_add(request: HttpRequest, slug: str):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    cart.add(product)
    return redirect('products:list')
