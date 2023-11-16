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


def send_step(update, context, step_id):
    if step_id:
        buttons = get_buttons(step_id)
        step = get_step(step_id)
    else:
        buttons = [{"text": "/start"}]
        step = {"text": "Мы вернулись к началу диалога. Нажмите /start"}

    keyboard = [
        [KeyboardButton(button['text'])] for button in buttons
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        one_time_keyboard=True,
    )

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=step['text'],
        reply_markup=reply_markup,
    )


def main_handler(update: Update, context: CallbackContext):
    step_id = context.user_data.get('step_id', 0)
    data = fetch_from_db(step_id)
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
