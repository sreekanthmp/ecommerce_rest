# Generated by Django 4.0.5 on 2022-08-03 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_order_customer'),
        ('user', '0014_remove_user_first_name_remove_user_last_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
