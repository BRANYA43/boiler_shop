from carts.cart import Cart

from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.views.generic import FormView

from orders.forms import CustomerForm
from orders.models import Customer, Order, OrderProduct
from orders.views import MakeOrderView

from products.tests.test_model import create_test_product


class MakeOrderSuccessMessageView(TestCase):
    def setUp(self) -> None:
        self.url = reverse('orders:make_order_success_message')

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'orders/make_order_success_message.html')

    def test_view_contains_message(self):
        message = "Thank you for your order. We'll phone you soon for information clarification."
        response = self.client.get(self.url)
        self.assertContains(response, message)


class MakeOrderViewTest(TestCase):
    def setUp(self) -> None:
        self.post_data = {'first_name': 'First name', 'last_name': 'Last name', 'phone': '0505555555'}
        self.url = reverse('orders:make_order')

    def test_view_inherits_necessary_generics(self):
        self.assertTrue(issubclass(MakeOrderView, FormView))

    def test_view_uses_correct_template_GET(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'orders/make_order.html')

    def test_view_passes_CustomerForm_to_context_GET(self):
        response = self.client.get(self.url)
        form = response.context['form']
        self.assertIsInstance(form, CustomerForm)

    def test_view_passes_Cart_to_context_GET(self):
        response = self.client.get(self.url)
        cart = response.context['cart']
        self.assertIsInstance(cart, Cart)

    def test_view_creates_customer_if_form_is_valid_POST(self):
        self.assertEqual(0, Customer.objects.count())

        self.client.post(self.url, data=self.post_data)

        self.assertEqual(1, Customer.objects.count())

    def test_view_doesnt_create_customer_if_form_is_invalid_POST(self):
        self.assertEqual(0, Customer.objects.count())

        self.client.post(self.url, data={})

        self.assertEqual(0, Customer.objects.count())

    def test_view_adds_new_customer_id_to_session_POST(self):
        self.client.post(self.url, data=self.post_data)
        customer = Customer.objects.first()

        self.assertEqual(self.client.session['cart']['customer'], customer.pk)

    def test_view_creates_new_order_POST(self):
        self.assertEqual(0, Order.objects.count())

        self.client.post(self.url, data=self.post_data)

        self.assertEqual(1, Order.objects.count())

    def test_view_creates_order_products_from_cart_POST(self):
        request = HttpRequest()
        request.session = self.client.session
        cart = Cart(request)
        cart.add(create_test_product(name='name-1', slug='slug-1'))
        cart.add(create_test_product(name='name-2', slug='slug-2'))

        self.assertEqual(0, OrderProduct.objects.count())

        self.client.post(self.url, data=self.post_data)

        self.assertEqual(2, OrderProduct.objects.count())

    def test_view_redirects_to_success_message_if_form_is_valid_POST(self):
        response = self.client.post(self.url, data=self.post_data)
        self.assertRedirects(response, reverse('orders:make_order_success_message'))

    def test_after_make_order_cart_is_clear(self):
        request = HttpRequest()
        request.session = self.client.session
        cart = Cart(request)
        cart.add(create_test_product())

        self.client.post(self.url, data=self.post_data)

        self.assertFalse(self.client.session['cart']['products'])
