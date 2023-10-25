from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from products.tests.test_model import create_test_product


class RenameImageFilenameTest(TestCase):
    def setUp(self) -> None:
        self.image = SimpleUploadedFile("test_image.png", b"file_content", content_type="image/png")
        self.product = create_test_product()

    def tearDown(self) -> None:
        if self.product.image.name is not None:
            self.product.image.delete()

    def test_signal_doesnt_rename_filename_if_image_is_empty(self):
        self.assertIsNone(self.product.image.name)

        self.product.slug = 'new_slug'
        self.product.save()

        self.assertIsNone(self.product.image.name)

    def test_signal_rename_filename_if_slug_is_changed(self):
        self.product.image = self.image
        self.product.save()

        self.assertIn(self.product.slug, self.product.image.name)

        self.product.slug = 'new_slug'
        self.product.save()

        self.assertIn(self.product.slug, self.product.image.name)

    def test_signal_doesnt_rename_filename_if_slug_is_not_changed(self):
        self.product.image = self.image
        self.product.save()
        old_image_name = self.product.image.name

        self.assertIn(self.product.slug, old_image_name)

        self.product.name = 'new_name'
        self.product.save()

        self.assertIn(self.product.slug, old_image_name)
