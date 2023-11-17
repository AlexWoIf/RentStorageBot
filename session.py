import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Session


def start_session(user):
    Session.objects.create(
        user=user
    )


def add_step_to_session(session, step):
    session.steps.add(step)


