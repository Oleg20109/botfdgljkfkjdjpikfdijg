import telebot

token=('8227926192:AAEmQTkvDjQ7Mog21vP6JTiCOFA5jmm4Ezg')
bot=telebot.TeleBot(token)
@bot.message_handler(command=['start'])
def hello2(message):
    bot.send_message(message, "hello")
    bot.infinity_polling()