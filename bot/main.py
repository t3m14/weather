from aiogram import Bot, Dispatcher
import asyncio
import os
import requests as req
from aiogram.filters import CommandStart

bot = Bot(token='6372656273:AAFuVcjyknS7NaM7rS1sod6UBqgt_zhIM60')
# bot = Bot(token=os.environ.get('TELEGRAM_TOKEN'))
dp = Dispatcher()
# Weather bot

# Start command handler
@dp.message(CommandStart())
async def start_command(message):
    await message.answer('Привет! Я бот, который покажет тебе погоду в любом городе России. Напиши мне название города')

# Weather by city name handler
@dp.message()
async def weather_by_city_name(message):
    city_name = message.text
    request_url = os.environ.get("BACKEND_URL") + f"/weather/?city={city_name}"
    response = req.get(request_url)
    if response.status_code == 200:
        weather_data = response.json()
        city_name = weather_data['city_name']
        url = weather_data['url']
        wind_speed = weather_data['wind_speed']
        temparature = weather_data['temparature']
        pressure = weather_data['pressure']
    
        await message.answer(f'Погода в городе {city_name}:\nВетер {wind_speed} м/с\nТемпература {temparature}°C\nДавление {pressure} мм рт. ст.\n\nПодробнее: {url}')
    else:
        await message.answer('Что-то не понял, посмотри-ка лучше в окно!')
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())