import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Session, Customer, Step


def get_or_create_user(name, telegram_id):
    Customer.objects.get_or_create(
        name=name,
        telegram_id=telegram_id
    )


# создаем или берем юзера, возвращаем последний шаг его сессии
def get_or_create_session(telegram_id):
    user = Customer.objects.get_or_create(
        telegram_id=telegram_id
    )
    session = Session.objects.get_or_create(
        user=user
    )

    return session.steps.last()


def add_step_to_session(telegram_id, step_id):
    user = Customer.objects.get(
        telegram_id=telegram_id
    )
    session = Session.objects.get(user=user)
    step = Step.objects.get(
        id=step_id
    )
    session.steps.add(step)


def remove_last_step_from_session(telegram_id):
    user = Customer.objects.get(
        telegram_id=telegram_id
    )
    session = Session.objects.get(user=user)
    last_step = session.steps.last()
    session.steps.remove(last_step)

    return last_step.id
