# Generated by Django 4.2.7 on 2023-11-19 18:56

from django.db import migrations


def change_next_step(apps, schema_editor):
    Button = apps.get_model('storage', 'Button')
    Step = apps.get_model('storage', 'Step')
    buttons = [
        {
            "step": "Выбор боксов new 1",
            "text": "Своими силами",
        },
        {
            "step": "Выбор боксов new 2",
            "text": "Бесплатная доставка из дома",
        }
    ]
    for button in buttons:
        step = Step.objects.get(name=button['step'])

        new_button = Button.objects.get(
            text=button['text']
        )

        new_button.next_step = step
        new_button.save()


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0030_auto_20231119_1537'),
    ]

    operations = [
        migrations.RunPython(change_next_step)
    ]