import telebot #импорт библиотеки
import config
import random

bot = telebot.TeleBot(config.TOKEN) # подключение токена бота из файла в этой же директории config.py после импорта Telebot (также можно в скобках ('%ваш токен%'))

# В этом участке кода мы объявили слушателя для текстовых сообщений и метод их обработки. Поле content_types может принимать разные значения
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
        # отработка кнопки старт
        if message.text == "/start":
                bot.send_message(message.from_user.id, "Введите нужное количество скороговорок или выберите в меню")
        
        # !!! вводят текст, имеющий в себе только цифру от 1 до 30
        elif message.text.isdigit() == True: # проверка если введенный текст целое число и выполняется int
                if int(message.text) in [k for k in range(1,31)]:
                        for i in range (int(message.text)):
                                c = random.choice(open('list.txt').readlines())
                                bot.send_message(message.from_user.id, c)
                elif int(message.text) > 30:
                                bot.send_message(message.from_user.id, "Введено слишком большое число, максимально доступный вывод - 30 штук")
                else:
                        bot.send_message(message.from_user.id, "Некорректный запрос")

        # отработка кнопок меню (сделать одним елифом и одной функцией)
        elif message.text == "/1":
                c = random.choice(open('list.txt').readlines())
                bot.send_message(message.from_user.id, c)
        elif message.text == "/5":
                for i in range (5):
                        c = random.choice(open('list.txt').readlines())
                        bot.send_message(message.from_user.id, c)
        elif message.text == "/10":
                for i in range (10):
                        c = random.choice(open('list.txt').readlines())
                        bot.send_message(message.from_user.id, c)
        else:
                bot.send_message(message.from_user.id, "Некорректный запрос")

#RUN
bot.polling(none_stop=True)