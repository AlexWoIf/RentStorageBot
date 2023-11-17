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


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, LOG_LEVEL.upper(), None),
    filename='bot.log',
)


START = 'START'


def send_step(update, context, step_name):
    if step_name != START:
        data = fetch_from_db(step_name)
        buttons = data['buttons']
        step_text = data['text']
    else:
        buttons = ["/start"]
        step_text = "Мы вернулись к началу диалога. Нажмите /start"

    keyboard = [
        [KeyboardButton(button)] for button in buttons
    ]
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
    step_name = context.user_data.get('step_name', START)
    if step_name == START:
        buttons = ['/start',]
    else:
        data = fetch_from_db(step_name)
        buttons = data['buttons']
    logging.debug(f'{step_name=} {buttons=}')
    for button in buttons:
        logging.debug(f'{update.message.text=} {button=}')
        if button in update.message.text:
            next_step = button
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
