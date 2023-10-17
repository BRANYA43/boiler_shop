from base.models import DateModelMixin, NameModelMixin

from ckeditor.fields import RichTextField

from django.db import models
from django.test import TestCase
from django.urls import reverse

from ..models import Product


def create_test_product() -> Product:
    return Product.objects.create(name='name', slug='slug', price=9999)


class ProductTest(TestCase):
    def test_product_inherit_needed_model_mixin(self):
        self.assertTrue(issubclass(Product, NameModelMixin))
        self.assertTrue(issubclass(Product, DateModelMixin))

    def test_price_field(self):
        field: models.DecimalField = Product._meta.get_field('price')

        self.assertIsInstance(field, models.DecimalField)

    def test_specifications_field(self):
        field: RichTextField = Product._meta.get_field('specifications')

        self.assertIsInstance(field, RichTextField)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_description_field(self):
        field: RichTextField = Product._meta.get_field('description')

        self.assertIsInstance(field, RichTextField)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_get_absolute_url(self):
        product = create_test_product()
        self.assertEqual(product.get_absolute_url(), reverse('products:detail', args=[product.slug]))
