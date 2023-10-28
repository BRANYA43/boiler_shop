import uuid

from base.models import DateModelMixin
from base.unit_tests.model_test import ModelTest

from django.db import models

from products.models import Product

from ..models import Customer, Order, OrderProduct, PhoneField


def create_test_customer(first_name='First name', last_name='Last name', phone='(050) 555 55-55') -> Customer:
    return Customer.objects.create(first_name=first_name, last_name=last_name, phone=phone)


def create_test_order(customer: Customer) -> Order:
    return Order.objects.create(customer=customer)


def create_test_order_product(order: Order, product: Product, name=None, price=None, quantity=1) -> OrderProduct:
    if name:
        product.name = name
        product.save()
    if price:
        product.price = price
        product.save()

    name = product.name
    price = product.price
    return OrderProduct.objects.create(order=order, product=product, name=name, price=price, quantity=quantity)


class OrderModelTest(ModelTest):
    def test_model_inherits_necessary_mixins(self):
        self.assertTrue(issubclass(Order, DateModelMixin))

    def test_model_has_uuid_field(self):
        field: models.UUIDField = self.get_field(Order, 'uuid')

        self.assertIsInstance(field, models.UUIDField),
        self.assertIs(field.default, uuid.uuid4)

    def test_model_has_customer_field(self):
        field: models.ForeignKey = self.get_field(Order, 'customer')

        self.assertIsInstance(field, models.ForeignKey)


class OrderProductModelTest(ModelTest):
    def test_model_has_order_field(self):
        field: models.ForeignKey = self.get_field(OrderProduct, 'order')

        self.assertIsInstance(field, models.ForeignKey)

    def test_model_has_product_field(self):
        field: models.ForeignKey = self.get_field(OrderProduct, 'product')

        self.assertIsInstance(field, models.ForeignKey)

    def test_model_has_name_field(self):
        field: models.CharField = self.get_field(OrderProduct, 'name')

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 50)

    def test_model_has_price_field(self):
        field: models.DecimalField = self.get_field(OrderProduct, 'price')

        self.assertIsInstance(field, models.DecimalField)

    def test_model_has_quantity_field(self):
        field: models.PositiveIntegerField = self.get_field(OrderProduct, 'quantity')

        self.assertIsInstance(field, models.PositiveIntegerField)


class CustomerModelTest(ModelTest):
    def test_model_inherits_necessary_mixins(self):
        self.assertTrue(issubclass(Customer, DateModelMixin))

    def test_model_has_first_name_field(self):
        field: models.CharField = self.get_field(Customer, 'first_name')

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 50)

    def test_model_has_last_name_field(self):
        field: models.CharField = self.get_field(Customer, 'last_name')

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 50)

    def test_model_has_phone_field(self):
        field: PhoneField = self.get_field(Customer, 'phone')

        self.assertIsInstance(field, PhoneField)
