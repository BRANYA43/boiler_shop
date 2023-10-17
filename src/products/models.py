from base.models import DateModelMixin, NameModelMixin

from django.db import models
from django.urls import reverse_lazy


class Product(NameModelMixin, DateModelMixin):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse_lazy('products:detail', args=[self.slug])
