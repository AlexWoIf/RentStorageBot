import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Session


def start_session(user):
    Session.objects.create(
        user=user
    )


#поменять session на юзера
def add_step_to_session(session, step):
    session.steps.add(step)

#добавить def remove_step_from_session(user, step)