from uuid import uuid4

from base.models import DateModelMixin

from django.db import models

from orders.validators import validate_phone

from products.models import Product


class PhoneField(models.CharField):
    default_validators = [validate_phone]

    def __init__(self, *args, max_length=20, **kwargs):
        super().__init__(*args, max_length=max_length, **kwargs)


class Customer(DateModelMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneField()


class Order(DateModelMixin):
    uuid = models.UUIDField(default=uuid4)
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT, related_name='orders')


class OrderProduct(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, related_name='order_products', null=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
