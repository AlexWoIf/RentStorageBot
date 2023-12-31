# Generated by Django 4.2.7 on 2023-11-19 11:58

from django.db import migrations


def sort_buttons(apps, schema_editor):
    Step = apps.get_model('storage', 'Step')
    steps = [
            "Приветствие",
            "Правила аренды",
            "Контакты",
            "Способ складирования",
            "Выбор боксов 1",
            "Срок аренды",
            "Номер телефона",
            "Имя",
            "Подтверждение 1",
            "QR-код",
            "Стоимость",
            "Курьер",
            "Подтверждение 2",
            "Выбор бокса 2",
            "Номер телефона 2",
    ]
    for step in steps:
        new_step = Step.objects.get(name=step)
        new_step.buttons.all().order_by('order')


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0026_delivery_customer_delivery_status'),
    ]

    operations = [
        migrations.RunPython(sort_buttons)
    ]
