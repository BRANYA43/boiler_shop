from django.http import HttpRequest

from orders.models import Customer

from products.models import Product


class Cart:
    def __init__(self, request: HttpRequest):
        self._session = request.session
        self._customer = None
        self._set_products()
        self.save()

    def _set_products(self):
        if self._session.get('cart'):
            self._products = self._session['cart']['products']
        else:
            self._products = {}

    @property
    def products(self) -> dict:
        return self._products.copy()

    @property
    def customer(self) -> Customer:
        if self._customer:
            return Customer.objects.get(id=self._customer)

    @customer.setter
    def customer(self, customer: Customer):
        self._customer = customer.pk
        self.save()

    def __eq__(self, other):
        return {'products': self._products, 'customer': self._customer} == other

    def __iter__(self):
        for slug, quantity in self._products.items():
            yield Product.objects.get(slug=slug), quantity

    def save(self):
        self._session['cart'] = {'products': self._products, 'customer': self._customer}
        self._session.save()

    def add(self, product: Product):
        self._products[product.slug] = 1
        self.save()
