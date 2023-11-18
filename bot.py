import logging
from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    CallbackContext,
    MessageHandler,
    Filters,
)
from fetch_from_db import fetch_from_db
from settings import LOG_LEVEL, BOT_TOKEN

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfStorage.settings')
django.setup()
from storage.models import Step


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, LOG_LEVEL.upper(), None),
    filename='bot.log',
)


START = 0
BACK = 'Назад'


def send_step(update, context, step_id):
    if step_id != START:
        step = Step.objects.get(id=step_id)
        buttons = step.buttons.all()
        step_text = step.text
        keyboard = [
            [KeyboardButton(button.text)] for button in buttons
        ]
    else:
        keyboard = [["/start"]]
        step_text = "Мы вернулись к началу диалога. Нажмите /start"

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        one_time_keyboard=True,
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=step_text,
        reply_markup=reply_markup,
    )


def main_handler(update: Update, context: CallbackContext):
    step_id = context.user_data.get('step_id', 0)
    logging.debug(f'{step_id=}')
    if not step_id:
        if '/start' in update.message.text:
            context.user_data['step_id'] = 1
            send_step(update, context, 1)
        return
    step = Step.objects.get(id=step_id)
    buttons = step.buttons.all()
    logging.debug(f'{step=} {buttons=}')
    for button in buttons:
        logging.debug(f'{update.message.text=} {button=}')
        if button.text in update.message.text:
            if button.text == BACK:
                continue
            next_step = button.next_step.id
            if not next_step:
                next_step = 0
            context.user_data['step_id'] = next_step
            send_step(update, context, next_step)
            return

    # тут обрабатываем пользовательский ввод если он присутствует
    # в данном шаге (и то что не подходит под команды на кнопках)


# функция main
if __name__ == '__main__':
    updater = Updater(
                    token=f'{BOT_TOKEN}',
                    use_context=True,
    )
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, main_handler))

    updater.start_polling()
    # обработчик нажатия Ctrl+C
    updater.idle()
