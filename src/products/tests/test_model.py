from base.models import DateModelMixin, NameModelMixin

from django.db import models
from django.test import TestCase

from products.models import Product


class ProductTest(TestCase):
    def test_product_inherit_needed_model_mixin(self):
        self.assertTrue(issubclass(Product, NameModelMixin))
        self.assertTrue(issubclass(Product, DateModelMixin))

    def test_price_field(self):
        field: models.DecimalField = Product._meta.get_field('price')

        self.assertIsInstance(field, models.DecimalField)
