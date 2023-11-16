def fill_up_buttons(apps, schema_editor):
    Button = apps.get_model('storage', 'Button')
    buttons = [
        {
            "step_id": 1,
            "text": "Правила размещения",
            "next_step": 2
        },
        {
            "step_id": 1,
            "text": "Контакты",
            "next_step": 3
        },
        {
            "step_id": 1,
            "text": "Выбрать бокс",
            "next_step": 4
        },
        {
            "step_id": 1,
            "text": "Забрать вещи",
            "next_step": 255
        },
        {
            "step_id": 2,
            "text": "Контакты",
            "next_step": 3
        },
        {
            "step_id": 2,
            "text": "Выбрать бокс",
            "next_step": 4
        },
        {
            "step_id": 2,
            "text": "Назад",
            "next_step": 1
        },
        {
            "step_id": 2,
            "text": "Выбрать бокс",
            "next_step": 4
        },
        {
            "step_id": 2,
            "text": "Назад",
            "next_step": 1
        },
        {
            "step_id": 2,
            "text": "Своими силами",
            "next_step": 255
        },
        {
            "step_id": 2,
            "text": "Бесплатная доставка из дома",
            "next_step": 255
        },
        {
            "step_id": 3,
            "text": "Выбрать бокс",
            "next_step": 255
        },
        {
            "step_id": 3,
            "text": "Назад",
            "next_step": 1
        },
        {
            "step_id": 0,
            "text": "/start",
            "next_step": 1
        }
    ]