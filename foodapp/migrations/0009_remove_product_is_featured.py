# Generated by Django 4.0.4 on 2022-05-18 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0008_remove_category_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_featured',
        ),
    ]
