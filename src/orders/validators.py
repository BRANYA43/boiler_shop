import re

from django.core.exceptions import ValidationError


def validate_phone(value):
    result = re.findall(r'\d', value)
    if len(result) != 10 and len(result) != 12:
        raise ValidationError('Phone number must have 10 or 12 digits')

    if re.search(r'[^\d\s\-()+]', value):
        raise ValidationError('Phone number can only contain digits, parentheses, space and hyphen')
