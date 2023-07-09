import telebot
import pyowm

API_key = '58fd0f20571c169dfcbd6ddff281b087'
owm = pyowm.OWM(API_key)
owm.config["language"] = "ru"
mgr = owm.weather_manager()

bot = telebot.TeleBot('6375384126:AAEE5TWlkjEXx5BIDAEWoGogLXKyy7JzHtA')


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    wind_speed = w.wind()['speed']
    humidity = w.humidity
    answer = f"""В городе {message.text} сейчас {w.detailed_status}, 
температура {int(temp)} гр., 
ветер {int(wind_speed)} м/с, 
влажность воздуха {humidity}%\n"""
    if temp < -19:
        answer += 'На улице дубак, одевайся потеплее'
    elif - 10 > temp > -18:
        answer += 'На улице терпимо, но надо одеваться тепло'
    elif - 5 > temp > -9:
        answer += 'На улице тепло, но всё же одевайся тепло'
    elif 8 > temp > -4:
        answer += 'На улице тепло, терпимо'
    elif 18 > temp > 9:
        answer += 'Тепло там'
    elif 25 > temp > 19:
        answer += 'Температура замечательная'
    else:
        answer += 'На улице жара'
    #bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
