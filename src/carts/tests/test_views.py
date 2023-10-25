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


class CartViewTest(TestCase):
    def setUp(self) -> None:
        self.cart_view_url = reverse('carts:cart')

    def test_view_uses_correct_template(self):
        response = self.client.get(self.cart_view_url)
        self.assertTemplateUsed(response, 'carts/cart.html')

    def test_view_have_only_added_products(self):
        added_product = create_test_product(name='Added product', slug='added_slug')
        not_added_product = create_test_product(name='Not added product', slug='not_added_slug')
        self.client.post(reverse('carts:cart_add', args=[added_product.slug]))
        response = self.client.get(self.cart_view_url)

        self.assertContains(response, added_product.name)
        self.assertNotContains(response, not_added_product.name)
