from django.test import TestCase
from django.urls import reverse
from django.views import generic

from .test_model import create_test_product
from .. import views


class ProductListViewTest(TestCase):
    def test_view_inherit_necessary_generic_view(self):
        self.assertTrue(issubclass(views.ProductListView, generic.ListView))

    def test_view_use_correct_template(self):
        response = self.client.get(reverse('products:list'))

        self.assertTemplateUsed(response, 'products/list.html')


class ProductDetailViewTest(TestCase):
    def test_view_inherit_necessary_generic_view(self):
        self.assertTrue(issubclass(views.ProductDetailView, generic.DetailView))

    def test_view_use_correct_template(self):
        product = create_test_product()
        response = self.client.get(reverse('products:detail', args=[product.slug]))

        self.assertTemplateUsed(response, 'products/detail.html')
