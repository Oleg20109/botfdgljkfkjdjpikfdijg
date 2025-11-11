import telebot
import g4f
token='8387116067:AAG2K6naPAa-wibXaEq-f_QRmUy4-Dxh5-I'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет напиши запрос')
@bot.message_handler()
def start_message(message):
    response = g4f.ChatCompletion.create(
        model=("gpt-4"),
        messages=[{
            "role": "user",
            'content': message.text}]
    )
    bot.send_message(message.chat.id, f'{response}')


bot.polling(True)