# Generated by Django 4.0.5 on 2022-08-21 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_customer'),
        ('order', '0017_remove_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='cart.cart'),
        ),
    ]
