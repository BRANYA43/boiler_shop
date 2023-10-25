# Generated by Django 4.2.6 on 2023-10-18 14:30

from django.db import migrations, models

import products.utils


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_description_product_specifications_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=products.utils.get_upload_path),
        ),
    ]