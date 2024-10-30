import asyncio # встроенный модуль для работы с асинхронностью
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command

from bs4 import BeautifulSoup
import requests

from config import token

bot = Bot(token=token)

dp = Dispatcher()

@dp.message(CommandStart()) 
async def start(message: types.Message):
    await message.answer("Привет")

@dp.message(Command('parsing'))
async def parsing_comm(message: types.Message):
    
    response = requests.get(url="https://www.sulpak.kg/")
    soup = BeautifulSoup(response.text, "lxml")

    title = soup.find_all("div", class_="product__item-name")
    prices = soup.find_all("div", class_="product__item-price")

    for name, price in zip(title, prices):
        await message.answer(f"\nНазвание товара - {name.text} - цена - {price.text}")


@dp.message()
async def echo(message: types.Message):
    await message.answer("Я вас не понял")


async def main():
    logging.basicConfig(level="INFO")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")