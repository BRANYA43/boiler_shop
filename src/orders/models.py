from django.db import models

from orders.validators import validate_phone


class PhoneField(models.CharField):
    default_validators = [validate_phone]

    def __init__(self, *args, max_length=20, **kwargs):
        super().__init__(*args, max_length=max_length, **kwargs)
