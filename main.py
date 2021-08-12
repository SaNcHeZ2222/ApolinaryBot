import time
import telebot
import config
import pymysql

bot = telebot.TeleBot(config.token)


def get_message_from_file(filename):
    with open(f'messages/{filename}', 'r', encoding='utf-8') as read_file:
        return read_file.read()


@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Узнать информацию через чат-бота', callback_data='Чат-бот'))
    markup.add(telebot.types.InlineKeyboardButton('Узнать информацию по телефону', callback_data='Запись'))
    bot.send_message(chat_id, get_message_from_file('start_message.txt'), reply_markup=markup)


@bot.callback_query_handler(func=lambda c: True)
def callback_reader(callback):
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    if callback.data == 'Чат-бот':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Низкодоходные и низкорисковые компании', callback_data='Низкие компании'))
        markup.add(telebot.types.InlineKeyboardButton('Высокодоходные и высокорисковые компании', callback_data='Высокие компании'))
        bot.send_message(chat_id, 'Выберите о каких компаниях хотите узнать, компании деляться на два типо, низкодоходные и высокодоходные', reply_markup=markup)
    if callback.data == 'Меню выбор большие и малые риски':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Низкодоходные и низкорисковые компании', callback_data='Низкие компании'))
        markup.add(telebot.types.InlineKeyboardButton('Высокодоходные и высокорисковые компании', callback_data='Высокие компании'))
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Выберите о каких компаниях хотите узнать, компании деляться на два типа, низкодоходные и высокодоходные', reply_markup=markup)
    if callback.data == 'Низкие компании':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Вернуться в выбор риска и дохода компаний', callback_data='Меню выбор большие и малые риски'))
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Вот список низкорисковых компаний', reply_markup=markup)
    if callback.data == 'Высокие компании':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('It Smart Money', callback_data='It Smart Money'))
        markup.add(telebot.types.InlineKeyboardButton('R-Coin', callback_data='R-Coin'))
        markup.add(telebot.types.InlineKeyboardButton('Senexa', callback_data='Senexa'))
        markup.add(telebot.types.InlineKeyboardButton('Вернуться в выбор риска и дохода компаний', callback_data='Меню выбор большие и малые риски'))
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Вот список низкорисковых компаний', reply_markup=markup)
    if callback.data == 'It Smart Money':
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Зарегистрироваться', url='google.com'))
        markup.add(telebot.types.InlineKeyboardButton('Презентация компании', callback_data='Презентация It Smart Money'))
        markup.add(telebot.types.InlineKeyboardButton('Инструкция по регистрации', callback_data='It Smart Money Instr'))
        markup.add(telebot.types.InlineKeyboardButton('Вернуться к списку высокорисковых и высокодоходных компаний', callback_data='Высокие компании'))
        bot.send_message(chat_id=chat_id, text=get_message_from_file('it_smart_money.txt'), reply_markup=markup)
    if callback.data == 'Презентация It Smart Money':
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Вернуться к It Smart Money', callback_data='It Smart Money'))
        doc = open('presentations/Презентация IT SMART MONEY.pdf', 'rb')
        bot.send_document(chat_id, doc, reply_markup=markup)
        doc.close()
    if callback.data == 'It Smart Money Instr':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Вернуться к компании It Smart Money', callback_data='It Smart Money'))
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=get_message_from_file('it_smart_money_instruction.txt'), reply_markup=markup)
    if callback.data == 'R-Coin':
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Зарегистрироваться', url='google.com'))
        markup.add(telebot.types.InlineKeyboardButton('Презентация компании', callback_data='Презентация R-Coin'))
        markup.add(telebot.types.InlineKeyboardButton('Вернуться к списку высокорисковых и высокодоходных компаний', callback_data='Высокие компании'))
        bot.send_message(chat_id, get_message_from_file('R-Coin.txt'), reply_markup=markup)
    if callback.data == 'Презентация R-Coin':
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Вернуться к R-Coin', callback_data='R-Coin'))
        doc = open('presentations/Презентация R-Coin.pdf', 'rb')
        bot.send_document(chat_id, doc, reply_markup=markup)
        doc.close()
    if callback.data == 'Senexa':
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Зарегистрироваться', url='google.com'))
        markup.add(telebot.types.InlineKeyboardButton('Презентация компании', callback_data='Презентация Senexa'))
        markup.add(telebot.types.InlineKeyboardButton('Вернуться к списку высокорисковых и высокодоходных компаний', callback_data='Высокие компании'))
        bot.send_message(chat_id, get_message_from_file('Senexa.txt'), reply_markup=markup)
    if callback.data == 'Презентация Senexa':
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton('Вернуться к Senexa', callback_data='Senexa'))
        doc = open('presentations/SENEXA rus Presentation.pdf', 'rb')
        bot.send_document(chat_id, doc, reply_markup=markup)
        doc.close()


while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(e)
        time.sleep(10)
