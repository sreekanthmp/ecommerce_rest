# Generated by Django 4.0.5 on 2022-08-25 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0033_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='orderstatus',
        ),
    ]
