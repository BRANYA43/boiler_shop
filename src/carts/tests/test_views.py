from django.test import TestCase
from django.urls import reverse

from products.tests.test_model import create_test_product


class CartSetQuantity(TestCase):
    def setUp(self) -> None:
        self.product = create_test_product()
        session = self.client.session
        session['cart'] = {'products': {self.product.slug: 1}}
        session.save()
        self.url = reverse('carts:cart_set_quantity', args=[self.product.slug])
        self.post_data = {'quantity': 100}

    def test_view_redirects_to_cart(self):
        response = self.client.post(self.url, data=self.post_data)
        self.assertRedirects(response, reverse('carts:cart'))

    def test_view_set_new_quantity(self):
        self.client.post(self.url, data=self.post_data)
        self.assertEqual(100, self.client.session['cart']['products'][self.product.slug])


class CartClearTest(TestCase):
    def setUp(self) -> None:
        self.product_1 = create_test_product(name='product_1', slug='slug_1')
        self.product_2 = create_test_product(name='product_2', slug='slug_2')
        session = self.client.session
        session['cart'] = {'products': {self.product_1.slug: 1}}
        session['cart']['products'][self.product_2.slug] = 1
        session.save()
        self.url = reverse('carts:cart_clear')

    def test_view_redirects_to_cart(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('carts:cart'))

    def test_view_clears_cart(self):
        self.client.get(self.url)
        self.assertFalse(self.client.session['cart']['products'])


class CartRemoveTest(TestCase):
    def setUp(self) -> None:
        self.product = create_test_product()
        session = self.client.session
        session['cart'] = {'products': {self.product.slug: 1}}
        session.save()
        self.url = reverse('carts:cart_remove', args=[self.product.slug])

    def test_view_redirects_to_cart(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('carts:cart'))

    def test_view_removes_product_from_cart(self):
        self.client.get(self.url)

        self.assertNotIn(self.product.slug, self.client.session['cart']['products'])


class CartAddTest(TestCase):
    def setUp(self) -> None:
        self.product = create_test_product()
        self.url = reverse('carts:cart_add', args=[self.product.slug])
        self.data = {'last_url': reverse('products:list')}

    def test_view_get_only_POST(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_view_redirects_to_last_page(self):
        response = self.client.post(self.url, data=self.data)
        self.assertRedirects(response, reverse('products:list'))

    def test_view_adds_product_to_cart(self):
        self.client.post(self.url, data=self.data)
        self.assertIn(self.product.slug, self.client.session['cart']['products'])


class CartViewTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('carts:cart')

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'carts/cart.html')

    def test_view_have_only_added_products(self):
        added_product = create_test_product(name='Added product', slug='added_slug')
        not_added_product = create_test_product(name='Not added product', slug='not_added_slug')

        session = self.client.session
        session['cart'] = {'products': {added_product.slug: 1}}
        session.save()

        response = self.client.get(self.url)

        self.assertContains(response, added_product.name)
        self.assertNotContains(response, not_added_product.name)
