from base.models import DateModelMixin, NameModelMixin
from base.unit_tests.model_test import ModelTest

from ckeditor.fields import RichTextField

from django.db import models
from django.urls import reverse

from ..models import Product
from ..utils import get_upload_path


def create_test_product(name='name', slug='slug', price=9999) -> Product:
    return Product.objects.create(name=name, slug=slug, price=price)


class ProductTest(ModelTest):
    def test_product_inherit_needed_model_mixin(self):
        self.assertTrue(issubclass(Product, NameModelMixin))
        self.assertTrue(issubclass(Product, DateModelMixin))

    def test_price_field(self):
        field: models.DecimalField = self.get_field(Product, 'price')

        self.assertIsInstance(field, models.DecimalField)

    def test_specifications_field(self):
        field: RichTextField = self.get_field(Product, 'specifications')

        self.assertIsInstance(field, RichTextField)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_description_field(self):
        field: RichTextField = self.get_field(Product, 'description')

        self.assertIsInstance(field, RichTextField)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_image_field(self):
        field: models.ImageField = self.get_field(Product, 'image')

        self.assertIsInstance(field, models.ImageField)
        self.assertTrue(field.null)
        self.assertIs(field.upload_to, get_upload_path)

    def test_get_absolute_url(self):
        product = create_test_product()
        self.assertEqual(product.get_absolute_url(), reverse('products:detail', args=[product.slug]))
