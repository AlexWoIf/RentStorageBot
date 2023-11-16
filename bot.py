import logging
from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
)
from settings import LOG_LEVEL, BOT_TOKEN

from steps_data import get_step, get_buttons

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, LOG_LEVEL.upper(), None),
    filename='bot.log',
)


def send_step(update, context, step_id):
    buttons = get_buttons(step_id)
    keyboard = [
        [KeyboardButton(button['text'])] for button in buttons
    ]
    logging.debug(f'{buttons=} {keyboard=}')
    reply_markup = ReplyKeyboardMarkup(keyboard)
    step = get_step(step_id)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=step['text'],
        reply_markup=reply_markup,
    )


def main_handler(update: Update, context: CallbackContext):
    step_id = context.user_data.get('step_id', 0)
    buttons = get_buttons(step_id)
    logging.debug(f'{step_id=} {buttons=}')
    for button in buttons:
        if button['text'] in update.message.text:
            next_step = button['next_step']
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
