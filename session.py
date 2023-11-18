import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Session


def get_or_create_session(user):
    session = Session.objects.get_or_create(
        user=user
    )

    return session

def add_step_to_session(user, step):
    session = Session.objects.get(user=user)
    session.steps.add(step)


def remove_last_step_from_session(user):
    session = Session.objects.get(user=user)
    last_step = session.steps.last()
    session.steps.remove(last_step)
