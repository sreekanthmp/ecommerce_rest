# Generated by Django 4.0.5 on 2022-08-20 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('order', '0015_alter_order_customer_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cart', to='cart.cart'),
        ),
    ]
