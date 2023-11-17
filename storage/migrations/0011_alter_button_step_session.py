# Generated by Django 4.2.7 on 2023-11-17 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0010_step_previous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='step',
            field=models.ManyToManyField(blank=True, related_name='buttons', to='storage.step', verbose_name='Прикрепленные шаги'),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.ManyToManyField(blank=True, related_name='sessions', to='storage.step', verbose_name='Прикрепленные шаги')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.customer', verbose_name='С кем сессия')),
            ],
        ),
    ]