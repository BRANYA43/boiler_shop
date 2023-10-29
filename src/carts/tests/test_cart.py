from django.http import HttpRequest
from django.test import TestCase

from orders.tests.test_models import create_test_customer

from products.models import Product
from products.tests.test_model import create_test_product

from ..cart import Cart


class CartTest(TestCase):
    def setUp(self) -> None:
        self.request = HttpRequest()
        self.request.session = self.client.session

    def test_init_cart(self):
        cart = Cart(self.request)

        self.assertEqual(cart.products, {})

    def test_init_cart_set_it_to_session(self):
        cart = Cart(self.request)

        self.assertEqual(cart, self.client.session['cart'])

    def test_init_cart_with_existing_cart_in_session(self):
        cart_data = {'products': {'slug': 1}, 'customer': None}
        self.request.session['cart'] = cart_data
        cart = Cart(self.request)

        self.assertEqual(cart, cart_data)

    def test_products_returns_copy_itself(self):
        cart = Cart(self.request)

        self.assertIsNot(cart.products, cart._products)
        self.assertEqual(cart.products, cart._products)

    def test_cart_is_iterable(self):
        new_product = create_test_product()
        cart = Cart(self.request)
        cart.add(new_product)
        for product, quantity in cart:
            self.assertIsInstance(product, Product)
            self.assertEqual(product.name, new_product.name)
            self.assertEqual(product.slug, new_product.slug)
            self.assertEqual(product.price, new_product.price)
            self.assertEqual(quantity, 1)

    def test_add_product_to_cart(self):
        cart = Cart(self.request)
        product = create_test_product()
        cart.add(product)

        self.assertEqual(cart.products, {product.slug: 1})

    def test_add_result_save_to_session(self):
        cart = Cart(self.request)
        product = create_test_product()
        cart.add(product)

        self.assertIn(product.slug, self.client.session['cart']['products'])
        self.assertEqual(1, self.client.session['cart']['products'][product.slug])

    def test_set_customer_for_cart(self):
        customer = create_test_customer()
        cart = Cart(self.request)
        cart.customer = customer

        self.assertEqual(cart.customer, customer)

    def test_set_customer_result_save_to_session(self):
        customer = create_test_customer()
        cart = Cart(self.request)
        cart.customer = customer

        self.assertEqual(customer.pk, self.client.session['cart']['customer'])

    def test_clear_cart(self):
        cart = Cart(self.request)
        cart.add(create_test_product())

        self.assertIsNotNone(cart.products)

        cart.clear()

        self.assertFalse(cart.products)
