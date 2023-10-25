from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models.signals import pre_save
from django.dispatch import receiver

from products.models import Product


@receiver(pre_save, sender=Product)
def rename_image_file_by_new_slug(sender, instance: Product, **kwargs):
    if instance.image.name is None:
        return
    elif instance.slug not in instance.image.name:
        instance.image = SimpleUploadedFile(instance.image.name, instance.image.read(), 'png')
