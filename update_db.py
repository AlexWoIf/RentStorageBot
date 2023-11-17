import os
from datetime import timedelta
import phonenumbers
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Container, Customer, Reservation, Delivery


def update_db(size, item, time, customer,
              phone_number, address, reservation, delivery=None):
    now_time = timezone.now()
    if not delivery:
        empty_containers = Container.objects.filter(
            available=True,
            size=size
        )
        container = empty_containers.first()

        new_customer = Customer.objects.create(
            name=customer,
            phone_number=phone_number
        )
        normal_number = phonenumbers.parse(
            new_customer.phone_number, "RU"
        )
        if phonenumbers.is_valid_number(normal_number):
            new_customer.pure_phone = normal_number
        new_customer.save()

        new_reservation = Reservation.objects.create(
            customer=new_customer,
            address=address,
            start_date=now_time,
            end_date=now_time + timedelta(days=time)
        )

        container.available = False
        container.filled_by = item
        container.reserved_by = new_customer
        container.reservation = new_reservation
    else:
        container = Container.objects.get(
            reservation=reservation
        )
        new_delivery = Delivery.objects.create(
            date=delivery
        )
        container.delivery = new_delivery
    container.save()

