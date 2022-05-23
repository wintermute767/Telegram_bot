import telebot
from config import TOKEN, keys
from extensions import APIException, ConvertionException, СurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n \
<имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n \
Количество валюты можно указать в десятичных числах с точкой.\n \
Для получения списка всех доступных валют введите команду:/values"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise APIException('Неверное количество аргументов')

        base, quote, amount=values
        result = round(СurrencyConverter.get_price(base, quote, amount), 2)

    except APIException as e:
        bot.reply_to(message, f"Не удалось обработать команду,\nвведите команду еще раз.\nОшитка:{e}")
    except Exception as e:
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:


        text = f'Цена {amount} {base} в {quote} = {result}'
        bot.send_message(message.chat.id, text)
bot.polling()