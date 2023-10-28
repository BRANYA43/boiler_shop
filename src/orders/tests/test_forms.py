from django.test import TestCase

from .test_models import create_test_customer
from ..forms import CustomerForm
from ..models import Customer


class CustomerFormTest(TestCase):
    def setUp(self) -> None:
        self.data = {'first_name': 'First name', 'last_name': 'Last name', 'phone': '0505555555'}

    def test_form_changes_phone_by_pattern_for_correct_format(self):
        form = CustomerForm(data={'phone': '0505555555'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['phone'], '38(050) 555 55-55')

    def test_form_save_returns_new_customer(self):
        form = CustomerForm(data=self.data)
        form.is_valid()

        self.assertEqual(0, Customer.objects.count())

        form.save()

        self.assertEqual(1, Customer.objects.count())

    def test_form_save_doesnt_create_new_customer_if_customer_with_such_phone_is_existing(self):
        create_test_customer()
        form = CustomerForm(data=self.data)
        form.is_valid()

        self.assertEqual(1, Customer.objects.count())

        form.save()

        self.assertEqual(1, Customer.objects.count())

    def test_form_save_returns_existing_customer_if_customer_with_such_phone_is_existing(self):
        existing_customer = create_test_customer()
        form = CustomerForm(data=self.data)
        form.is_valid()
        form_customer = form.save()

        self.assertEqual(form_customer.pk, existing_customer.pk)
