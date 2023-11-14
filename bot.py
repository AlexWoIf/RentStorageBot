import logging
from telegram import Update
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    Filters,
)
from settings import LOG_LEVEL, BOT_TOKEN


STARTED = 1


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, LOG_LEVEL.upper(), None),
    filename='bot.log',
)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Рад что Вы заинтересовались нашим сервисом!\n'
             'Ниже расположены кнопки с вашими возможными вопросами 👇',
    )
    return STARTED


def help(update, context):
    pass


# функция main
if __name__ == '__main__':
    updater = Updater(
                    token=f'{BOT_TOKEN}',
                    use_context=True,
    )
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
                CommandHandler('start', start),
        ],
        states={
            STARTED: [
            ],
        },
        fallbacks=[]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    # обработчик нажатия Ctrl+C
    updater.idle()
