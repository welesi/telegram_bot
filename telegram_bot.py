import telebot
import requests

API_TOKEN = '8038506076:AAG03MaU3vODYfwu_7s_XOcDc66LKbMrWK4'
WEATHER_API_KEY = '4de4e822e77c2d3a20fad3c834f793f6'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city_name = message.text
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

        reply = f"Погода в {city}:\nТемпература: {temperature}°C\nОписание: {weather_description.capitalize()}"
    else:
        reply = "Город не найден. Пожалуйста, проверьте название города и попробуйте снова."

    bot.reply_to(message, reply)


# Запускаем бота
bot.polling(none_stop=True)
