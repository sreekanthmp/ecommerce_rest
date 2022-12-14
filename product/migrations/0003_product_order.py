# Generated by Django 4.0.5 on 2022-07-31 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_customer_remove_order_product'),
        ('product', '0002_product_delete_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to='order.order'),
            preserve_default=False,
        ),
    ]
