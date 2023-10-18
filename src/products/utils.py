import os.path
from pathlib import Path

from django.conf import settings


def get_upload_path(instance, filename: str) -> Path:
    extension = filename.split('.')[-1]
    filename = f'{instance.slug}.{extension}'
    path = Path(os.path.join('products/images/', filename))
    if os.path.exists(settings.MEDIA_ROOT / path):
        os.remove(settings.MEDIA_ROOT / path)
    return path
