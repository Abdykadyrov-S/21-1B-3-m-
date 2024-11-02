import asyncio # встроенный модуль для работы с асинхронностью
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command

from config import token

"""
Bot - Абстрактный класс для того что бы создать объект класса

Dispatcher - посредник 

types - модуль в aiogram

CommandStart - класс для создания комманды start

Command - класс для создания комманд
"""


bot = Bot(token=token)

dp = Dispatcher()

"""
@dp.message - хендлер (обработчик(перехватчик) сообщений)

"""


@dp.message(CommandStart()) 
# /start == сообщению который отправил пользователь
# if message.text == '/start: # True
    # start()
# else:
    # pass
async def start(message: types.Message):
    await message.answer("Привет")

@dp.message(Command('help'))
# /help == сообщению который отправил пользователь
# if message.text == '/help: # True
    # help_comm()
# else:
    # pass
async def help_comm(message: types.Message):
    await message.reply('Чем могу помочь?')

@dp.message(Command('play'))
async def play_comm(message: types.Message):
    await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg', caption="Вы выиграли")

@dp.message(F.text == "Привет")
async def echo(message: types.Message):
    await message.answer("Привет, как дела?")

@dp.message(F.text.in_({"Привет", 'привет', "hi", "как дела"}))
async def echo(message: types.Message):
    await message.answer("Привет, как дела?")

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