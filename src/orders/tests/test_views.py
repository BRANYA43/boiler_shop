from django.test import TestCase
from django.urls import reverse


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
