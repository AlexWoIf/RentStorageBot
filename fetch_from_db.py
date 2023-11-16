import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Step


def fetch_from_db(step, previous_step=None):
    fetched_step = Step.objects.get(name=step)
    name = fetched_step.name
    text = fetched_step.text
    buttons = fetched_step.buttons.all()
    step_params = {
        'name': name,
        'text': text,
        'buttons': [button.text for button in buttons]
    }
    if not previous_step:
        return step_params
    else:
        step_params['previous'] = Step.objects.get(name=previous_step)
        return step_params
