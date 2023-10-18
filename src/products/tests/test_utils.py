from pathlib import Path
from unittest.mock import Mock, patch

from django.conf import settings
from django.test import TestCase

from ..utils import get_upload_path


class GetUploadPathTest(TestCase):
    def test_get_upload_path_returns_correct_path(self):
        instance = Mock(slug='slug')
        filename = 'some_image.png'
        path = get_upload_path(instance, filename)
        correct_path = Path(f'products/images/{instance.slug}.png')

        self.assertEqual(path, correct_path)

    @patch('os.path.exists', return_value=True)
    @patch('os.remove')
    def test_get_upload_path_removes_existing_file_by_path(self, mock_remove: Mock, mock_exists: Mock):
        instance = Mock(slug='slug')
        filename = 'some_image.png'

        path = get_upload_path(instance, filename)

        mock_exists.assert_called_once_with(settings.MEDIA_ROOT / path)
        mock_remove.assert_called_once_with(settings.MEDIA_ROOT / path)
