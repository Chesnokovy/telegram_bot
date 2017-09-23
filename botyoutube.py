# -*- coding: utf-8 -*-
import telebot
import config
bot = telebot.TeleBot(config.token)
print(bot.get_me())
print("\n-----")
def log(message,answer):
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,message.from_user.last_name,str (message.from_user.id),message.text))
    print(answer)
@bot.message_handler(content_types =['text'])
user_markup = telebot.types.replykeyboardmarkup()
bot.polling(none_stop=True,interval=0)