# Generated by Django 5.0.2 on 2024-03-04 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='category',
        ),
    ]
