# Generated by Django 4.2.7 on 2023-11-17 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0014_rename_name_customer_first_name_customer_is_bot_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
    ]