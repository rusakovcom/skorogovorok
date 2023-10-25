import telebot # import of the telebot library, which is used for creating and managing Telegram bots with Python.
from telebot import types # import module for keyboard in the chat
import random # import library for random choise

bot = telebot.TeleBot('TOKEN') # TOKEN and creating the object of the bot


@bot.message_handler(commands=['start']) # Create reciever of the start command
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True) # Create keyboard with types of answer
    
    button1 = types.KeyboardButton("1")
    button5 = types.KeyboardButton("5")
    button3 = types.KeyboardButton("3")
    button10 = types.KeyboardButton("10")
    
    markup.add(button1, button3, button5, button10)
    
    # send message to user with keyboard
    bot.send_message(message.chat.id, "Выберите в меню какое количество скороговорок вывести:", reply_markup=markup)


@bot.message_handler(func=lambda message: True) # Create reciever of the buttons text and any other incorrect input
def handle_number(message):
    if message.text == "1":
        c = random.choice(open('list.txt').readlines())
        bot.send_message(message.from_user.id, c)
    elif message.text == "3":
        for i in range (3):
            c = random.choice(open('list.txt').readlines())
            bot.send_message(message.from_user.id, c)
    elif message.text == "5":
        for i in range (5):
            c = random.choice(open('list.txt').readlines())
            bot.send_message(message.from_user.id, c)
    elif message.text == "10":
        for i in range (10):
            c = random.choice(open('list.txt').readlines())
            bot.send_message(message.from_user.id, c)
    else:
        bot.send_message(message.from_user.id, "Выберите в меню какое количество скороговорок вывести:")


bot.polling(none_stop=True) # continue send requests to Telegram servers for getting new messages by users