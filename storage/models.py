from django.db import models


class Customer(models.Model):
    name = models.CharField('Имя клиента', max_length=100)
    phone_number = models.CharField('Номер клиента', max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    type = models.CharField(
        'Тип предмета',
        max_length=50
    )


class Container(models.Model):
    size = models.CharField(
        max_length=20,
        verbose_name='Размер контейнера'
    )
    available = models.BooleanField(
        verbose_name='Свободен ли контейнер',
        null=True, blank=True,
        choices=(
            (True, 'Свободен'),
            (False, 'Занят'),
        )
    )
    start_date = models.DateTimeField(
        'Когда контейнер был занят',
        null=True, blank=True
    )
    end_date = models.DateTimeField(
        'Когда контейнер освободится',
        null=True, blank=True
    )
    reserved_by = models.ForeignKey(
        Customer,
        verbose_name='Кем занят',
        related_name='containers',
        null=True, blank=True,
        on_delete=models.CASCADE
    )
    filled_by = models.ForeignKey(
        Item,
        verbose_name='Чем заполнен',
        null=True, blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Контейнер {self.pk}'
