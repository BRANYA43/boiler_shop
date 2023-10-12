from django.test import TestCase
from django.urls import reverse
from django.views.generic import ListView

from ..views import ProductListView


class ProductListViewTest(TestCase):
    def test_view_inherit_needed_generic_view(self):
        self.assertTrue(ProductListView, ListView)

    def test_view_use_needed_template(self):
        response = self.client.get(reverse('products:list'))

        self.assertTemplateUsed(response, 'products/list.html')
