from base.models import DateModelMixin, NameModelMixin

from ckeditor.fields import RichTextField

from django.db import models
from django.urls import reverse_lazy

from .utils import get_upload_path


class Product(NameModelMixin, DateModelMixin):
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specifications = RichTextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('products:detail', args=[self.slug])

    def __str__(self):
        return f'{self.name}'
