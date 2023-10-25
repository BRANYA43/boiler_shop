from django.test import TestCase
from django.urls import reverse

from products.tests.test_model import create_test_product


class CartAddTest(TestCase):
    def setUp(self) -> None:
        self.product = create_test_product()
        self.cart_add_url = reverse('carts:cart_add', args=[self.product.slug])

    def test_view_redirects_to_correct_page(self):
        response = self.client.post(self.cart_add_url)
        self.assertRedirects(response, reverse('products:list'))

    def test_view_adds_product_to_cart(self):
        self.client.post(self.cart_add_url)
        self.assertIn(self.product.slug, self.client.session['cart'].keys())
