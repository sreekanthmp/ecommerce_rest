# Generated by Django 4.0.5 on 2022-08-02 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_customer'),
        ('user', '0007_remove_customer_age_remove_customer_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customer',
        ),
    ]
