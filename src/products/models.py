from base.models import DateModelMixin, NameModelMixin

from django.db import models


class Product(NameModelMixin, DateModelMixin):
    price = models.DecimalField(max_digits=10, decimal_places=2)
