# Generated by Django 4.2.7 on 2023-11-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0017_customer_self_name_customer_telegram_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Место кнопки'),
        ),
    ]