from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from products.models import Product

from .cart import Cart


def cart_set_quantity(request: HttpRequest, slug: str):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    cart.set_quantity(product, int(request.POST['quantity']))
    return redirect('carts:cart')


def cart_clear(request: HttpRequest):
    cart = Cart(request)
    cart.clear()
    return redirect('carts:cart')


def cart_remove(request: HttpRequest, slug: str):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    cart.remove(product)
    return redirect('carts:cart')


@require_POST
def cart_add(request: HttpRequest, slug: str):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    cart.add(product)
    return redirect(request.POST['last_url'])


def cart_view(request: HttpRequest):
    cart = Cart(request)
    return render(request, 'carts/cart.html', {'cart': cart})
