# Generated by Django 4.0.5 on 2022-08-01 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
    ]
