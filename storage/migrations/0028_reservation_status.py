# Generated by Django 4.2.7 on 2023-11-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0027_auto_20231119_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Ждет поступления'), (2, 'На складе'), (3, 'Выполнено')], null=True, verbose_name='Статус заявки'),
        ),
    ]
