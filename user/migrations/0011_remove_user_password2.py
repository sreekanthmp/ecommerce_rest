# Generated by Django 4.0.5 on 2022-08-03 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]
