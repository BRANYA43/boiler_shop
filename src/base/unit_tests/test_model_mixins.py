from django.db import models
from django.test import TestCase

from ..models import DateModelMixin, NameModelMixin


class MixinTest(TestCase):
    @staticmethod
    def create_test_model(base_class):
        test_model = type('TestModel', (base_class,), {'__module__': base_class.__module__})
        return test_model()


class NameModelMixinTest(MixinTest):
    def setUp(self):
        self.test_model = self.create_test_model(NameModelMixin)

    def test_model_is_abstract(self):
        self.assertTrue(NameModelMixin._meta.abstract)

    def test_name_field(self):
        field: models.CharField = self.test_model._meta.get_field('name')
        self.assertTrue(isinstance(field, models.CharField))
        self.assertEqual(field.max_length, 50)

    def test_slug_field(self):
        field: models.SlugField = self.test_model._meta.get_field('slug')
        self.assertTrue(isinstance(field, models.SlugField))
        self.assertEqual(field.max_length, 50)

    def test_get_absolute_url_method(self):
        with self.assertRaises(NotImplementedError):
            self.test_model.get_absolute_url()


class DateModelMixinTest(MixinTest):
    def setUp(self):
        self.test_model = self.create_test_model(DateModelMixin)

    def test_model_is_abstract(self):
        self.assertTrue(DateModelMixin._meta.abstract)

    def test_created_field(self):
        field: models.DateTimeField = self.test_model._meta.get_field('created')
        self.assertTrue(isinstance(field, models.DateTimeField))
        self.assertTrue(field.auto_now_add)

    def test_updated_field(self):
        field: models.DateTimeField = self.test_model._meta.get_field('updated')
        self.assertTrue(isinstance(field, models.DateTimeField))
        self.assertTrue(field.auto_now)
