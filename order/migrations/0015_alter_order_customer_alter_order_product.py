# Generated by Django 4.0.5 on 2022-08-09 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0014_alter_order_customer_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='product.product'),
        ),
    ]
