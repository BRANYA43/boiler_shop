from django.http import HttpRequest
from django.shortcuts import redirect, render

from products.models import Product

from .cart import Cart


def cart_add(request: HttpRequest, slug: str):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    cart.add(product)
    return redirect('products:list')


def cart_view(request: HttpRequest):
    cart = Cart(request)
    return render(request, 'carts/cart.html', {'cart': cart})
