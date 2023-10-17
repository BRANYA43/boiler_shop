from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
