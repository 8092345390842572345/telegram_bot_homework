import telebot
from telebot import types
import math

# список команд: send, register, start, help

API_TOKEN = "1219283344:AAHNXmHuA8MltzpFJ5CLsPLaU5zMitTxN4o"    # токен бота

bot = telebot.TeleBot(API_TOKEN)

text1 = "send"                                                  # первый текст на кнопке клавиатуры
text2 = "изменить данные учетной записи"                        # второой текст на кнопке клавиатуры
text3 = "/register"

meetingText = "О, ты снова тут"                                 # приветственный текст
registerText = 'введите свой класс и паралель через точку. \nПример: "8.6"'
errorText = "ошибка"
helpText = "Короче, Меченый, я получил /help и в благородство играть не буду: получишь пару объяснений - и мы в расчете. \n Вот тебе список команд: \n /start – ты просто начнёшь всё сначала, и дело с концом\n /send – тебе придётся выбрать предмет, но это не самое сложное. Самое сложное - послать дз после этого \n/register – как правило нужно в начале нового учебного года. Ты просто укажешь параллель и всех учителей как в первый раз. \n/help – команда, которую ты только что использовал, видимо бошка после амнезии не прояснилась"

# /money – бот кинет тебе реквизиты разрабов, а ты делай с этой информацией что захочешь. Желательно кинешь деньги.

@bot.message_handler(commands=['1895001123581321345589'])
def file_output(message):
    doc = open("data.txt", "a+")
    chat_id = message.chat.id
    bot.send_document(chat_id, doc)
    doc.close()


@bot.message_handler(commands=['start'])
def send_welcome(message):                                      # приветственная функция 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text1, text3) 
    msg = bot.reply_to(message, meetingText, reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)


@bot.message_handler(commands=['help'])
def help_function(message):                                      # функция help с описанием возможностей
    msg = bot.reply_to(message, helpText)
    bot.register_next_step_handler(msg, process_step)


@bot.message_handler(commands=['register'])
def register_function(message):
    msg = bot.reply_to(message, registerText)
    bot.register_next_step_handler(msg, register_set)
    

def register_set(message):      
    doc = open("data.txt", "a+")                                # функция обработки паралели и класса при регистрации
    chat_id = message.chat.id
    msg = bot.reply_to(message, chat_id)
    doc.write(str(chat_id))
    doc.close()
    try:
        class_num = float(message.text)
    except BaseException:
        msg = bot.reply_to(message, errorText)


def process_step(message):                                      # функция обработки кастомной клавиатуры бота
    chat_id = message.chat.id

bot.polling()