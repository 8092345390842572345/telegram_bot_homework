import telebot
from telebot import types
import math

# список команд: send, register, start, help
# process_step заменить на несколько обработчиков


file = open("data.txt", 'w')                                    # файл с данными пользователей
file.close()

API_TOKEN = "**********************************************"    # токен бота

bot = telebot.TeleBot(API_TOKEN)

text1 = "send"                                                  # первый текст на кнопке клавиатуры
text2 = "изменить данные учетной записи"                        # второой текст на кнопке клавиатуры
text3 = "/register"

fileText = "."

meetingText = "О, ты снова тут"                                 # приветственный текст
registerText = 'введите свой класс и паралель через точку. \nПример: "8.6"'
errorText = "ошибка"
helpText = "Короче, Меченый, я получил /help и в благородство играть не буду: получишь пару объяснений - и мы в расчете. \n Вот тебе список команд: \n /start – ты просто начнёшь всё сначала, и дело с концом\n /send – тебе придётся выбрать предмет, но это не самое сложное. Самое сложное - послать дз после этого \n/register – как правило нужно в начале нового учебного года. Ты просто укажешь параллель и всех учителей как в первый раз. \n/help – команда, которую ты только что использовал, видимо бошка после амнезии не прояснилась"

# /money – бот кинет тебе реквизиты разрабов, а ты делай с этой информацией что захочешь. Желательно кинешь деньги.
'''
def get_text():
    file = open("data.txt", "r")
    for line in file:
        fileText = fileText + line + "\n"
    file.close()
get_text()
'''


@bot.message_handler(commands=['**********************'])      
def file_output(message):                                      # функция help с описанием возможностей
    # get_text()
    chat_id = message.chat.id
    doc = open("data.txt", 'rb')
    msg = bot.reply_to(message, fileText)
    bot.send_document(chat_id, doc)
    bot.send_document(chat_id, "FILEID") 


@bot.message_handler(commands=['start'])
def send_welcome(message):                                      # приветственная функция 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True)
    # markup.add(text1, text2, text3) 
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
    

def register_set(message):                                      # функция обработки паралели и класса при регистрации
    chat_id = message.chat.id
    msg = bot.reply_to(message, chat_id)
    file = open("data.txt", "w")
    file.write(str(chat_id))
    file.close()
    try:
        class_num = float(message.text)
    except BaseException:
        msg = bot.reply_to(message, errorText)
        # bot.register_next_step_handler(msg)
    # if message.text==text1:
        # func1()
    # else:
        # func2()


def process_step(message):                                      # функция обработки кастомной клавиатуры бота
    chat_id = message.chat.id
    # if message.text==text1:
        # func1()
    # else:
        # func2()
bot.polling()
# file.close()


'''
старый и бесполезный код

import telebot

bot = telebot.TeleBot("1219283344:AAHNXmHuA8MltzpFJ5CLsPLaU5zMitTxN4o")

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('send', 'изменить данные учетной записи')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.polling()
'''
