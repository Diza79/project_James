import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5174354002:AAGgC0vjmJPRJeeG2SrQ9KbRSTlYsRJ-YFM'

reply_keyboard = [['/start', '/information', '/help']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def words(update, context):
    update.message.reply_text(
        'Простите, но я вас не понимаю\n'
        'Используйте команды',
        reply_markup=markup
    )


def start(update, context):
    reply_keyboard_helping = [['/eat', '/sleep', '/recommend']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Здравствуйте! Я Джеймс, ваш гид по городу Барнаулу.\n"
        'Чем могу помочь?',
        reply_markup=markup_helping
    )


def recommend(update, context):
    reply_keyboard_helping = [['/museum', '/parks', '/theatre'],
                              ['/monuments', '/architecture'],
                              ['/start']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Рекомендуем посетить:",
        reply_markup=markup_helping
    )


def museum(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/музей'
    )


def parks(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/парки'
    )


def theatre(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/театры'
    )


def monuments(update, context):
    update.message.reply_text(
        'http://project27223.tilda.ws/'
    )


def architecture(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/памятники'
    )


# Функции для ЕДЫ START


def eat(update, context):
    reply_keyboard_helping = [['/coffee', '/restaurants', '/coffee_bar'],
                              ['/business_lunch', '/kitchen', '/vegetarian'],
                              ['/start']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Выберите ваши предпочтения",
        reply_markup=markup_helping
    )


def coffee(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Кофейня'
    )


def restaurants(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Ресторан'
    )


def coffee_bar(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Бар'
    )


def business_lunch(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Бизнес-ланч'
    )


def vegetarian(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/filter/type_cuisine/vegetarian_cuisine'
    )


# Функции для ВИДА КУХНИ START


def kitchen(update, context):
    reply_keyboard_helping = [['/japan', '/russian', '/italian', '/home', '/europa'],
                              ['/start', '/eat']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Выберите тип кухни",
        reply_markup=markup_helping
    )


def japan(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Ресторан/filter/type_cuisine/japanese_cuisine'
    )


def russian(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Ресторан/filter/type_cuisine/russian_cuisine'
    )


def italian(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Ресторан/filter/type_cuisine/italian_cuisine'
    )


def home(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Ресторан/filter/type_cuisine/home_cuisine'
    )


def europa(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Ресторан/filter/type_cuisine/european_cuisine'
    )


# END

# ОТЕЛИ


def sleep(update, context):
    reply_keyboard_helping = [['/hotel', '/hostels', '/sanatorium'],
                              ['/start']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Где вы хотите переночеввать?",
        reply_markup=markup_helping
    )


def hostels(update, context):
    reply_keyboard_helping = [['/hostel_3', '/hostel_4'],
                              ['/start', '/sleep']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Какая должна быть минимальная оценка поситителей?",
        reply_markup=markup_helping
    )


def hostels_3(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Хостел/filter/rating_threshold/gt3.0'
    )


def hostels_4(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Хостел/filter/rating_threshold/gt4.0'
    )


def sanatorium(update, context):
    reply_keyboard_helping = [['/sanatorium_3', '/sanatorium_4'],
                              ['/start', '/sleep']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Какая должна быть минимальная оценка поситителей?",
        reply_markup=markup_helping
    )


def sanatorium_3(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Санаторий/filter/rating_threshold/gt3.0'
    )


def sanatorium_4(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/search/Санаторий/filter/rating_threshold/gt4.0'
    )


def hotel(update, context):
    reply_keyboard_helping = [['/hotel_3', '/hotel_4'],
                              ['/start', '/sleep']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Какая должна быть минимальная оценка поситителей?",
        reply_markup=markup_helping
    )


def hotel_3(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/category/hotel/184106414/filter/rating_threshold/gt3.0'
    )


def hotel_4(update, context):
    update.message.reply_text(
        'https://yandex.ru/maps/197/barnaul/category/hotel/184106414/filter/rating_threshold/gt4.0'
    )


# END


def helping(update, context):
    reply_keyboard_helping = [['/start']]
    markup_helping = ReplyKeyboardMarkup(reply_keyboard_helping, one_time_keyboard=False)
    update.message.reply_text(
        "Я помогу вам в туризме по Барнаулу\n"
        "Введите команду /start, чтобы я начал работать",
        reply_markup=markup_helping
    )


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text & ~Filters.command, words)
    dp.add_handler(text_handler)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helping))

    dp.add_handler(CommandHandler('recommend', recommend))
    dp.add_handler(CommandHandler('parks', parks))
    dp.add_handler(CommandHandler('theatre', theatre))
    dp.add_handler(CommandHandler('monuments', monuments))
    dp.add_handler(CommandHandler('architecture', architecture))
    dp.add_handler(CommandHandler('museum', museum))

    dp.add_handler(CommandHandler("eat", eat))
    dp.add_handler(CommandHandler("coffee", coffee))
    dp.add_handler(CommandHandler("restaurants", restaurants))
    dp.add_handler(CommandHandler("coffee_bar", coffee_bar))
    dp.add_handler(CommandHandler("business_lunch", business_lunch))
    dp.add_handler(CommandHandler("vegetarian", vegetarian))
    dp.add_handler(CommandHandler("kitchen", kitchen))
    dp.add_handler(CommandHandler("japan", japan))
    dp.add_handler(CommandHandler("russian", russian))
    dp.add_handler(CommandHandler("italian", italian))
    dp.add_handler(CommandHandler("home", home))
    dp.add_handler(CommandHandler("europa", europa))

    dp.add_handler(CommandHandler("sleep", sleep))
    dp.add_handler(CommandHandler("hostels", hostels))
    dp.add_handler(CommandHandler("hostels_3", hostels_3))
    dp.add_handler(CommandHandler("hostels_4", hostels_4))
    dp.add_handler(CommandHandler("sanatorium", sanatorium))
    dp.add_handler(CommandHandler("sanatorium_3", sanatorium_3))
    dp.add_handler(CommandHandler("sanatorium_4", sanatorium_4))
    dp.add_handler(CommandHandler("hotel", hotel))
    dp.add_handler(CommandHandler("hotel_3", hotel_3))
    dp.add_handler(CommandHandler("hotel_4", hotel_4))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
