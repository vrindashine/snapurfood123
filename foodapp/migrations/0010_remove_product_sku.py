# Generated by Django 4.0.4 on 2022-05-18 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0009_remove_product_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
    ]