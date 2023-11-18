from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    name = models.CharField(
        'Имя клиента',
        max_length=100
    )
    last_name = models.CharField(
        'Имя клиента 2',
        max_length=100,
        null=True, blank=True
    )
    username = models.CharField(
        'Имя клиента 3',
        max_length=100,
        null=True, blank=True
    )
    self_name = models.CharField(
        'Имя клиента 4',
        max_length=100,
        null=True, blank=True
    )
    telegram_id = models.IntegerField(
        'id клиента',
        null=True, blank=True
    )
    phone_number = models.CharField(
        'Номер клиента',
        max_length=20,
        null=True, blank=True
    )
    pure_phone = PhoneNumberField(
        'Нормализованный Номер владельца',
        blank=True, null=True
    )
    is_bot = models.BooleanField(
        verbose_name='Бот или нет',
        null=True, blank=True
    )
    language_code = models.CharField(
        'Код языка', max_length=10,
        null=True, blank=True
    )

    def __str__(self):
        return self.name


class Reservation(models.Model):
    customer = models.ForeignKey(
        Customer,
        verbose_name='Кем был сделан заказ',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='reservations'
    )
    start_date = models.DateTimeField(
        'Начало срока хранения',
        null=True, blank=True
    )
    end_date = models.DateTimeField(
        'Окончание срока хранения',
        null=True, blank=True
    )
    address = models.CharField(
        'Адрес склада',
        max_length=100,
        null=True, blank=True
    )

    def __str__(self):
        return f'Заказ {self.pk}'


class Delivery(models.Model):
    date = models.DateTimeField(
        'Дата доставки',
        null=True, blank=True
    )

    def __str__(self):
        return f'Доставка {self.pk}'


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
    reservation = models.ForeignKey(
        Reservation,
        verbose_name='Заказ',
        null=True, blank=True,
        related_name='containers',
        on_delete=models.CASCADE
    )
    reserved_by = models.ForeignKey(
        Customer,
        verbose_name='Кем занят',
        related_name='containers',
        null=True, blank=True,
        on_delete=models.CASCADE
    )
    filled_by = models.CharField(
        'Чем заполнен',
        max_length=100,
        null=True, blank=True
    )
    delivery = models.ForeignKey(
        Delivery,
        verbose_name='Доставка',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='containers'
    )

    def __str__(self):
        return f'Контейнер {self.pk}'


class Step(models.Model):
    name = models.CharField(
        'Название шага',
        max_length=50,
        null=True, blank=True
    )
    text = models.TextField(
        'Текст сообщения в шаге',
        null=True, blank=True
    )
    previous = models.ForeignKey(
        'self',
        related_name='next',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name='Связь между шагами'

    )

    def __str__(self):
        return self.name


class Button(models.Model):
    step = models.ManyToManyField(
        Step,
        verbose_name='Прикрепленные шаги',
        blank=True,
        related_name='buttons'
    )
    text = models.CharField(
        'Текст кнопки',
        max_length=50,
        null=True, blank=True
    )
    order = models.IntegerField(
        'Место кнопки',
        null=True, blank=True
    )
    next_step = models.ForeignKey(
        Step,
        verbose_name='На какой шаг перейти',
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='from_button'
    )

    def __str__(self):
        return self.text


class Session(models.Model):
    user = models.OneToOneField(
        Customer,
        verbose_name='С кем сессия',
        null=True, blank=True,
        on_delete=models.CASCADE
    )
    steps = models.ManyToManyField(
        Step,
        verbose_name='Прикрепленные шаги',
        blank=True,
        related_name='sessions'
    )

    def __str__(self):
        return self.user.name
