# Generated by Django 4.0.5 on 2022-08-24 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_order'),
        ('cart', '0004_cart_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_price', to='product.product'),
        ),
    ]
