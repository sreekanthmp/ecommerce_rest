# Generated by Django 4.0.5 on 2022-08-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0034_rename_status_order_orderstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.IntegerField(null=True),
        ),
    ]