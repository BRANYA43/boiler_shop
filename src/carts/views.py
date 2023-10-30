from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from products.models import Product

from .cart import Cart


@require_POST
def cart_add(request: HttpRequest, slug: str):
    product = Product.objects.get(slug=slug)
    cart = Cart(request)
    cart.add(product)
    return redirect(request.POST['last_url'])


def cart_view(request: HttpRequest):
    cart = Cart(request)
    return render(request, 'carts/cart.html', {'cart': cart})
