import telebot
from telebot import types
import math
from token import API_TOKEN as tk

# список команд: send, register, start, help

bot = telebot.TeleBot(tk)

text1 = "send"                                                  # первый текст на кнопке клавиатуры
text2 = "изменить данные учетной записи"                        # второой текст на кнопке клавиатуры
text3 = "/register"
dct = {}

meetingText = "О, ты наконец-то тут"                                 # приветственный текст
registerText = 'Введи свой класс и паралель через точку. \nПример: "8.6"'
sendText = 'И вот наступил момент... когда тебе надо послать дз'
errorText = "ошибка"
helpText = "Короче, Меченый, я получил /help и в благородство играть не буду: получишь пару объяснений - и мы в расчете. \n Вот тебе список команд: \n /start – ты просто начнёшь всё сначала, и дело с концом\n /send – тебе придётся выбрать предмет, но это не самое сложное. Самое сложное - послать дз после этого \n/register – как правило нужно в начале нового учебного года. Ты просто укажешь параллель и всех учителей как в первый раз. \n/help – команда, которую ты только что использовал, видимо бошка после амнезии не прояснилась"

# /money – бот кинет тебе реквизиты разрабов, а ты делай с этой информацией что захочешь. Желательно кинешь деньги.

@bot.message_handler(commands=['1895001123581321345589'])
def file_output(message):
    pass


@bot.message_handler(commands=['start'])
def send_welcome(message):                                      # приветственная функция 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text3) 
    msg = bot.reply_to(message, meetingText, reply_markup=markup)


@bot.message_handler(commands=['send'])
def send(message):                                      # функция получения сообщения
    msg = bot.reply_to(message, sendText)
    bot.register_next_step_handler(msg, send_set)


def send_set(message):
    chat.id = message.chat.id
    doc = open("hw.jpeg", "a+")
    doc.write(message)
    doc.close()


@bot.message_handler(commands=['help'])
def help_function(message):                                      # функция help с описанием возможностей
    msg = bot.reply_to(message, helpText)


*@bot.message_handler(commands=['register'])
def register_function(message):
    msg = bot.reply_to(message, registerText)
    bot.register_next_step_handler(msg, register_set)
    

def register_set(message):                                      # функция обработки паралели и класса при регистрации
    chat_id = message.chat.id
    try:
        class_num = float(message.text)
        try:
            dct[chat_id]
    except BaseException:
        msg = bot.reply_to(message, errorText)


bot.polling()
