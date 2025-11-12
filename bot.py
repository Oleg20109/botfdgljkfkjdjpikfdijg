import telebot
import g4f
from g4f.client import Client

token='8387116067:AAG2K6naPAa-wibXaEq-f_QRmUy4-Dxh5-I'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здраствуйте напишите запрос для генерации изображения напишите /generation и после промт')

@bot.message_handler(commands=['generation'])
def generation(message):
    client = Client()
    response2 = client.images.generate(
        model=("flux"),
        prompt=message.text,
        response_format='url',
    )

    image = response2.data[0].url
    bot.send_message(message.chat.id, f'Ссылка на изображение{image}')


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