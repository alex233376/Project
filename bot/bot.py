import telebot
import config
# Получаем токен бота
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcom(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
                     parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.sed_message(message.chat.id, message.txt)


if __name__ == '__main__':
    bot.polling(none_stop=True)  # запуск бота
