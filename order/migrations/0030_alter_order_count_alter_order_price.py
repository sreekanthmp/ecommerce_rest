# Generated by Django 4.0.5 on 2022-08-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_alter_order_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
