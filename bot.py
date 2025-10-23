import telebot
from logic import timer
bot = telebot.TeleBot('YOUR TOKEN HERE')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот от allannar. Сейчас он в стадии разработки, но это временно... A little bit of waiting ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_help(massage):
    bot.reply_to(massage, 'Тут скоро появиться список команд бота, A little bit of waiting')

@bot.message_handler(commands=['info'])
def send_info(massage):
    bot.reply_to(massage, 'Тут скоро появиться информация о боте, A little bit of waiting')

#@bot.message_handler(commands=['generator'])
#def send_password(massage):

@bot.message_handler(commands=['timer'])
def send_timer(massage):
    bot.reply_to(massage, timer)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
