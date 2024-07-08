import telebot
from telebot import types

bot = telebot.TeleBot("7237356774:AAGovc39dJQRada88URlNR6JNuRKGiUp4AQ")

@bot.message_handler(commands=["start"])
def main(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("Информация")
    btn2 = types.KeyboardButton("Phone number")
    btn3 = types.KeyboardButton("Text")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Welcome to my bot", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Информация":
        bot.send_message(message.chat.id, "«Кунг-фу па́нда 4» — американо-китайский компьютерно-анимационный комедийный фильм о боевых искусствах, производством которого занимается студия DreamWorks Animation, а распространением — Universal Pictures. Четвёртый полнометражный фильм в медиафраншизе «Кунг-фу панда» и продолжение мультфильма «Кунг-фу панда 3»")
    elif message.text == "Phone number":
        bot.send_message(message.chat.id, "+996 704 352 535 --- Актай")
    elif message.text == "Text":
        bot.send_message(message.chat.id, "Кунг-фу Панда 4 мультфильм, 2024, дата выхода ...")



@bot.message_handler(content_types=['text'])
def get_info(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Кунфу Панда", url='https://kinogo.cm/19432-kung-fu-panda-4-hd-720-v1.html')
    markup.add(btn1)

    if message.text == "Кунфу Панда":
        bot.send_message(message.chat.id, "Кунфу Панда", reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, "Your are photo very good")

bot.polling(none_stop=True)

