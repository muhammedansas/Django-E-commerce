# Generated by Django 5.0.4 on 2024-05-06 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='product_category',
        ),
    ]