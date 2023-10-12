from django.db import models


class NameModelMixin(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        raise NotImplementedError


class DateModelMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
