# Generated by Django 5.0.4 on 2024-05-07 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_category_product_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='catogary',
        ),
    ]