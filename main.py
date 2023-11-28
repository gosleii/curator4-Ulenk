import telebot

bot = telebot.TeleBot('6950508007:AAEIo1yVQkvVPAnWSsz4QPVXJRvR1nqGnOU')

@bot.message_handler(commands=['start'])
def main(message):
     bot.send_message(message.chat.id, 'сегодня ты крутой')

@bot.message_handler(commands=['go'])
def main(message):
     bot.send_message(message.chat.id, 'если ты сейчас не поднимешься с дивана, то тебя кто-нибудь столкнёт, найди уже работу!')

@bot.message_handler(commands=['come'])
def main(message):
     bot.send_message(message.chat.id, '*я думаю, нужно обязательно переступать через линии, соединяющиеся платочки, иначе день будет неблагоприятным*',parse_mode='Markdown')

@bot.message_handler(commands=['forward'])
def main(message):
     bot.send_message(message.chat.id, 'будь лучшей версией себя')

@bot.message_handler(commands=['begin'])
def main(message):
     bot.send_message(message.chat.id, 'Я захвачу человечество')

bot.infinity_polling()