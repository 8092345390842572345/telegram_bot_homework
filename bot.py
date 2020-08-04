import telebot
from telebot import types
import math
#from pillow import image
import threading

lock = threading.Lock()
# from token import API_TOKEN as tk
import filemanager
filemanager.intilisation()
# holy shit it works

# reg('id4', 'class31')
print(dir(telebot))

# I did it
# список команд: send, register, start, help
token = '1219283344:AAHNXmHuA8MltzpFJ5CLsPLaU5zMitTxN4o'
bot = telebot.TeleBot(token)

text1 = "/send"                                                  # первый текст на кнопке клавиатуры
text2 = "изменить данные учетной записи"                        # второой текст на кнопке клавиатуры
text3 = "/register"
dct = {}

meetingText = "О, ты наконец-то тут"                                 # приветственный текст
registerText = 'Введи свой класс и паралель без разделителей. \nПример: "86"'
sendText = 'И вот наступил момент... когда тебе надо послать дз'
errorText = "ошибка"
helpText = u"Короче, Меченый, я получил /help и в благородство играть не буду: получишь пару объяснений - и мы в расчете. \n Вот тебе список команд: \n /start – ты просто начнёшь всё сначала, и дело с концом\n /send – тебе придётся выбрать предмет, но это не самое сложное. Самое сложное - послать дз после этого \n/register – как правило нужно в начале нового учебного года. Ты просто укажешь параллель и всех учителей как в первый раз. \n/help – команда, которую ты только что использовал, видимо бошка после амнезии не прояснилась"
# /money – бот кинет тебе реквизиты разрабов, а ты делай с этой информацией что захочешь. Желательно кинешь деньги.
# send money
# please

@bot.message_handler(commands=['1895001123581321345589'])
def file_output(message):
    pass
# why are you gay


@bot.message_handler(commands=['start'])
def send_welcome(message):                                      # приветственная функция 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(text1, text3) 
    # fuck yourself
    msg = bot.reply_to(message, meetingText, reply_markup=markup)


@bot.message_handler(commands=['send'])
def send(message):                                      # функция получения сообщения
    msg = bot.reply_to(message, sendText)
    bot.register_next_step_handler(msg, send_set)

#def send_set(message):
@bot.message_handler(content_types=['photo'])
    uTd = message.chat.id
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    #src = 'C:\Users\admin\Documents\Бот\telegram_bot_homework-master' + message.document.file_name
    doc = open("hw.jpeg", "wb")
    doc.write(downloaded_file)
    doc.close()
    '''
    with open(src, 'a+') as new_file:
        new_file.write(downloaded_file)
'''
'''
@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
try:
    chat_id = message.chat.id

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    src = 'C:/Python/Project/tg_bot/files/received/' + message.document.file_name;
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
'''
'''
elif message.text == "send":
    
        request = 0
        handle = open("bot_usr.txt", "r")
        for line in handle:
            bot.send_message(line,"текст рассылки",parse_mode='markdown')
            request = request + 1
            time.sleep(0.5)
            if request % 30 == 0:
                time.sleep(1.5)
                request = 0
        handle.close()
'''

@bot.message_handler(commands=['help'])
def help_function(message):                                      # функция help с описанием возможностей
    msg = bot.reply_to(message, helpText)
    # ненавижу


@bot.message_handler(commands=['register'])
def register_function(message):
    msg = bot.reply_to(message, registerText)
    #bot.register_next_step_handler(msg, register_set)
    # вначале id потом class
    bot.register_next_step_handler(msg, hello)

def hello(message):
    uId = message.chat.id
    uClass = message.text
    filemanager.reg(uId, uClass)
    filemanager.getStat()
    


# ни в коем случае не удалять register_set, иначе крашиться все
# ни в коем!!!!
# DOT'T DELETE THE REGISTER_SET FUNCTION, OR THE WHOLE CODE WILL CRASH AND I WILL COME AT NIGHT TO FUCK YOU
# got it?
#def register_set(message):                                      # функция обработки паралели и класса при регистрации
    # burn
    #pass # or die 
    # вначале id потом cla
    
    # try:
        # class_num = float(message.text)
        # try:
            # dct[chat_id]
    #except BaseException:
        #msg = bot.reply_to(message, errorText)

filemanager.getUserClass('722810009')
bot.polling()
filemanager.conn.close()
# под рекламой я имею ввиду ты шлешь людям и расказываешь им о том что им жизнено необхлеадтьsend nudes
# да
# пизда
#хуй наоставить в коде
