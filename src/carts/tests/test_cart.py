from django.http import HttpRequest
from django.test import TestCase

from products.tests.test_model import create_test_product

from ..cart import Cart


class CartTest(TestCase):
    def setUp(self) -> None:
        self.request = HttpRequest()
        self.request.session = self.client.session

    def test_init_cart_with_existing_cart_in_session(self):
        self.request.session['cart'] = {'slug': {}}
        cart = Cart(self.request)

        self.assertEqual(cart.cart, {'slug': {}})

    def test_init_cart_with_not_existing_cart_in_session(self):
        cart = Cart(self.request)

        self.assertEqual(cart.cart, {})

    def test_property_cart_returns_copy_itself(self):
        cart = Cart(self.request)
        self.assertIsNot(cart.cart, cart._cart)

    def test_save_cart_to_session(self):
        cart = Cart(self.request)
        cart._cart = {'test': 1}
        cart.save()

        self.assertEqual(cart.cart, self.request.session['cart'])

    def test_add_product_to_cart(self):
        cart = Cart(self.request)
        product = create_test_product()
        cart.add(product)

        self.assertEqual(cart.cart[product.slug], {'name': product.name, 'quantity': 1, 'price': str(product.price)})

    def test_add_result_save_to_session(self):
        cart = Cart(self.request)
        product = create_test_product()
        cart.add(product)

        self.assertIn(product.slug, self.request.session['cart'].keys())
