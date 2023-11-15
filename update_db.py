import os
from datetime import timedelta

import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Container, Item, Customer


def update_db(size, item, time, customer, phone_number):
    empty_containers = Container.objects.filter(
        available=True,
        size=size
    )
    now_time = timezone.now()
    new_customer = Customer.objects.create(
        name=customer,
        phone_number=phone_number
    )
    new_item = Item.objects.create(
        type=item,
    )
    container = empty_containers.first()
    container.available = False
    container.filled_by = new_item
    container.start_date = now_time
    container.end_date = now_time + timedelta(days=time)
    container.reserved_by = new_customer
    container.save()

