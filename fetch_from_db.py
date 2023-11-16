import os
from datetime import timedelta

import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()

from storage.models import Step


def fetch_from_db(step):
    fetched_step = Step.objects.get(name=step)
    text = fetched_step.text
    buttons = fetched_step.buttons.all()
    step_params = {
        'text': text,
        'buttons': [button.text for button in buttons]
    }

    return step_params
