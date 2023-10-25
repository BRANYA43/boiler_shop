from unittest import TestCase

from django.core.exceptions import ValidationError

from orders.validators import validate_phone


class ValidatePhoneTest(TestCase):
    def test_validator_raises_error_if_value_has_incorrect_digit_quantity(self):
        more_digits = '3805055555555'
        less_digits = '38050555555'
        with self.assertRaisesRegex(ValidationError, r'Phone number must have 10 or 12 digits'):
            validate_phone(more_digits)
            validate_phone(less_digits)

    @staticmethod
    def test_validator_doesnt_raise_error_if_value_has_correct_digit_quantity():
        correct_value_10 = '0505555555'
        correct_value_12 = '380505555555'

        validate_phone(correct_value_10)  # dont raises Exception
        validate_phone(correct_value_12)  # dont raises Exception

    def test_validator_raises_error_if_value_contain_forbidden_symbols(self):
        incorrect_value = '!@#%%^&380505555555adfasd'
        with self.assertRaisesRegex(
            ValidationError, r'Phone number can only contain digits, parentheses, space and hyphen'
        ):
            validate_phone(incorrect_value)

    @staticmethod
    def test_validator_doesnt_raise_error_if_value_doesnt_contain_forbidden_symbols():
        correct_value = '38 (050) 555 55-55'

        validate_phone(correct_value)  # dont raises Exception
