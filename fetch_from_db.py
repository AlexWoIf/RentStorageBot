import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Step


def fetch_from_db(step_id, previous_step_id=None):
    fetched_step = Step.objects.get(id=step_id)
    name = fetched_step.name
    text = fetched_step.text
    buttons = fetched_step.buttons.all()
    step_params = {
        'name': name,
        'text': text,
        'buttons': [button.text for button in buttons]
    }
    if not previous_step_id:
        return step_params
    else:
        fetched_step.previous = Step.objects.get(id=previous_step_id)
        fetched_step.save()
        step_params['previous'] = fetched_step.previous
        return step_params
