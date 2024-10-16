import asyncio 
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from config import token

bot = Bot(token=token)
dp = Dispatcher()

start_buttons = [
    [KeyboardButton(text="Шаурма🌯"), KeyboardButton(text="Бургер🍔")]
]

start_keyboard = ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)

sh_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Классическая")]])

@dp.message(CommandStart()) 
async def start(message: Message):
    await message.answer(f"Привет {message.from_user.full_name}", reply_markup=start_keyboard)

@dp.message(F.text == "Шаурма🌯")
async def shaurma(message: Message):
    await message.answer("""
                         ШАУРМА
Классическая - 180р
Шаурма XL - 180р""", reply_markup=sh_keyboard)
    # await message.answer_photo("https://s.prtv.su/wp-content/uploads/slajd_shaurma_vertikalnoe_menyu_chernyj_fon.jpg")

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    logging.basicConfig(level="INFO")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")