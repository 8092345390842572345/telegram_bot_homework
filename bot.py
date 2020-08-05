import telebot
from telebot import types
import math
import threading
import filemanager

lock = threading.Lock()
filemanager.intilisation()

token = '1219283344:AAHNXmHuA8MltzpFJ5CLsPLaU5zMitTxN4o'
bot = telebot.TeleBot(token)

text1 = "/send"                                                  # первый текст на кнопке клавиатуры
text2 = "/register"

meetingText = "О, ты наконец-то тут"                                 # приветственный текст
registerText = 'Введи свой класс и паралель без разделителей. \nПример: "86"'
sendText = 'И вот наступил момент... когда тебе надо послать дз'
errorText = "ошибка"

# 'u' - для форматирования текста в UTF-8
helpText = u'''
Короче, Меченый, я получил /help и в благородство играть не буду: получишь пару объяснений - и мы в расчете. \n 
Вот тебе список команд: \n /start – ты просто начнёшь всё сначала, и дело с концом\n 
/send – тебе придётся выбрать предмет, но это не самое сложное. Самое сложное - послать дз после этого \n
/register – как правило нужно в начале нового учебного года. Ты просто укажешь параллель и всех учителей как в первый раз. \n
/help – команда, которую ты только что использовал, видимо бошка после амнезии не прояснилась"
'''
# /money – бот кинет тебе реквизиты разрабов, а ты делай с этой информацией что захочешь. Желательно кинешь деньги.
# send money
# please

@bot.message_handler(commands=['start'])
def send_welcome(message):                                      # приветственная функция 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    # создает клавиатуру
    markup.add(text1, text2)                                    # форматирует ее
    msg = bot.reply_to(message, meetingText, reply_markup=markup)


@bot.message_handler(content_types=['photo']) # я хз как это работает...
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src='/home/lex/programs/python/telegram_bot/'+file_info.file_path;
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено") 
    except Exception as e:
        bot.reply_to(message,e )

@bot.message_handler(commands=['help'])
def help_function(message):                                      # функция help с описанием возможностей
    msg = bot.reply_to(message, helpText)


@bot.message_handler(commands=['register'])
def register_function(message):
    msg = bot.reply_to(message, registerText)
    # вначале id потом class
    bot.register_next_step_handler(msg, hello)

def hello(message):
    uId = message.chat.id
    uClass = message.text
    filemanager.reg(uId, uClass)
    filemanager.getStat()
    

filemanager.getUserClass('722810009')
bot.polling()
filemanager.conn.close()