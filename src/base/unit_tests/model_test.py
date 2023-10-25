from unittest import TestCase


class ModelTest(TestCase):
    @staticmethod
    def get_field(model, field_name: str):
        return model._meta.get_field(field_name)
