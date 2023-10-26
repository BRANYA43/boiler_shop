from django.http import HttpRequest

from products.models import Product


class Cart:
    def __init__(self, request: HttpRequest):
        self._session = request.session
        self._cart = self._session.get('cart', {})

    @property
    def cart(self) -> dict:
        return self._cart.copy()

    def save(self):
        self._session['cart'] = self._cart
        self._session.save()

    def add(self, product: Product):
        self._cart[product.slug] = {
            'name': product.name,
            'quantity': 1,
            'price': str(product.price),
        }
        self.save()
