# Generated by Django 4.0.5 on 2022-08-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0031_alter_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]