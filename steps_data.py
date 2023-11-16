#
# TODO: добавить кнопкам поле order
#
import json


j = '''
{"Step":[{
            "step_id": 1,
            "name": "",
            "text": "Этот Бот поможет вам хранить ваши вещи, когда в доме уже нет свободного места. Выберите нужные по размеру теплые боксы для хранения сезонных вещей, спортинвентаря и других личных вещей:"
        }, {
            "step_id": 2,
            "name": "",
            "text": "Скачайте файл с правилами  аренды: Тут файл с правилами или ссылка на него"
        }, {
            "step_id": 3,
            "name": "",
            "text": "Тут все адреса, номера телефонов почты и.т.д"
        }, {
            "step_id": 4,
            "name": "",
            "text": "Как бы вы хотели передать вещи на хранение? Доставщик замерит их габариты сам, либо их замерят при приёме на склад, если Вы выберете доставку своими силами."
        }
    ],
    "Button": [{
            "step_id": 1,
            "text": "Правила размещения",
            "next_step": 2
        },{
            "step_id": 1,
            "text": "Контакты",
            "next_step": 3
        },{
            "step_id": 1,
            "text": "Выбрать бокс",
            "next_step": 4
        },{
            "step_id": 1,
            "text": "Забрать вещи",
            "next_step": 255
        },{
            "step_id": 2,
            "text": "Контакты",
            "next_step": 3
        },{
            "step_id": 2,
            "text": "Выбрать бокс",
            "next_step": 4
        },{
            "step_id": 2,
            "text": "Назад",
            "next_step": 1
        },{
            "step_id": 2,
            "text": "Выбрать бокс",
            "next_step": 4
        },{
            "step_id": 2,
            "text": "Назад",
            "next_step": 1
        },{
            "step_id": 2,
            "text": "Своими силами",
            "next_step": 255
        },{
            "step_id": 2,
            "text": "Бесплатная доставка из дома",
            "next_step": 255
        },{
            "step_id": 3,
            "text": "Выбрать бокс",
            "next_step": 255
        },{
            "step_id": 3,
            "text": "Назад",
            "next_step": 1
        },{
            "step_id": 0,
            "text": "/start",
            "next_step": 1
        }
    ]
}
'''


data = json.loads(j)


Step = data['Step']
Button = data['Button']


def get_buttons(step_id):
    buttons = []
    for button in Button:
        if button['step_id'] == step_id:
            buttons.append(button)
    return buttons


def get_step(step_id):
    for step in Step:
        if step['step_id'] == step_id:
            return step
