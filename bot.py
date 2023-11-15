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
    ConversationHandler,
    Filters,
)
from settings import LOG_LEVEL, BOT_TOKEN


ENTRYPOINT, STARTED, RULES, CONTACTS, CHOOSE_BOX, TAKE_AWAY = range(6)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, LOG_LEVEL.upper(), None),
    filename='bot.log',
)


def start(update: Update, context: CallbackContext):
    button_list = [
        [KeyboardButton('Правила размещения')],
        [KeyboardButton('Контакты')],
        [KeyboardButton('Выбрать бокс')],
        [KeyboardButton('Забрать вещи')],
    ]
    reply_markup = ReplyKeyboardMarkup(button_list)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Этот Бот поможет вам хранить ваши вещи, когда в доме уже нет '
             'свободного места.\nВыберите нужные по размеру теплые боксы для '
             'хранения сезонных вещей, спортинвентаря и других личных вещей:',
        reply_markup=reply_markup,
    )
    return STARTED


def rules(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Скачайте файл с правилами  аренды:\n Тут файл с правилами или '
             'ссылка на него',
    )
    return RULES


def contacts(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=' Тут все адреса, номера телефонов почты и.т.д',
    )
    return CONTACTS


def choose_box(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Как бы вы хотели передать вещи на хранение?\nДоставщик замерит '
             'их габариты сам, либо их замерят при приёме на склад, если Вы '
             'выберете доставку своими силами.',
    )
    return CHOOSE_BOX


def take_away(update, context):
    button_list = [
        [KeyboardButton('Закакзать доставку')],
        [KeyboardButton('Контакты')],
        [KeyboardButton('Назад')],
    ]
    reply_markup = ReplyKeyboardMarkup(button_list)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Этот Бот поможет вам хранить ваши вещи, когда в доме уже нет '
             'свободного места.\nВыберите нужные по размеру теплые боксы для '
             'хранения сезонных вещей, спортинвентаря и других личных вещей:',
        reply_markup=reply_markup,
    )
    return TAKE_AWAY


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Вы ввели команду, которая отправляет на еще не созданный '
             'обработчик. Начните сначала.',
        reply_markup=ReplyKeyboardMarkup([]),
    )
    return 0


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
                MessageHandler(Filters.text('Правила размещения'), rules),
                MessageHandler(Filters.text('Контакты'), contacts),
                MessageHandler(Filters.text('Выбрать бокс'), choose_box),
                MessageHandler(Filters.text('Забрать вещи'), take_away),
            ],
            RULES: [],
            CONTACTS: [],
            CHOOSE_BOX: [],
            TAKE_AWAY: [
                MessageHandler(Filters.text('Заказать доставку'), rules),
                MessageHandler(Filters.text('Контакты'), contacts),
                MessageHandler(Filters.text('Назад'), start),
            ],
        },
        fallbacks=[]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    # обработчик нажатия Ctrl+C
    updater.idle()
