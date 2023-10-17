from django.test import TestCase
from django.urls import reverse
from django.views import generic

from .. import views


class ProductListViewTest(TestCase):
    def test_view_inherit_necessary_generic_view(self):
        self.assertTrue(issubclass(views.ProductListView, generic.ListView))

    def test_view_use_correct_template(self):
        response = self.client.get(reverse('products:list'))

        self.assertTemplateUsed(response, 'products/list.html')
