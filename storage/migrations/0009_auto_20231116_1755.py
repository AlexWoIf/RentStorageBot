# Generated by Django 4.2.7 on 2023-11-16 14:55

from django.db import migrations


def fill_up_buttons(apps, schema_editor):
    Button = apps.get_model('storage', 'Button')
    Step = apps.get_model('storage', 'Step')
    buttons = [
        {
            "step": ['Приветствие',],
            "text": "Правила размещения",
        },
        {
            "step": [
                'Приветствие',
                "Правила аренды",
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
                "Дата приезда"
            ],
            "text": "Контакты",
        },
        {
            "step": [
                'Приветствие',
                "Правила аренды",
                "Контакты"
            ],
            "text": "Выбрать бокс",
        },
        {
            "step": ['Приветствие',],
            "text": "Забрать вещи",
        },
        {
            "step": ["Способ складирования", ],
            "text": "Своими силами",
        },
        {
            "step": ["Способ складирования", ],
            "text": "Бесплатная доставка из дома",
        },
        {
            "step": [
                "Правила аренды",
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
                "Дата приезда",
                "Контакты"
            ],
            "text": "Назад",
        },
        {
            "step": ["Выбор боксов 1", ],
            "text": "1",
        },
        {
            "step": ["Выбор боксов 1", ],
            "text": "2",
        },
        {
            "step": ["Выбор боксов 1", ],
            "text": "3",
        }
    ]
    for button in buttons:
        steps = [Step.objects.get(name=step) for step in button['step']]

        new_button = Button.objects.create(
            text=button['text']
        )

        new_button.step.set(steps)


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0008_auto_20231116_1752'),
    ]

    operations = [
        migrations.RunPython(fill_up_buttons)
    ]
