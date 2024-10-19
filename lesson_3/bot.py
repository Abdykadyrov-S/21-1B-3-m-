import asyncio 
import logging
import sqlite3

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import token

bot = Bot(token=token)
dp = Dispatcher()


connection = sqlite3.connect("users.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS  users (
id INTEGER,
full_name VARCHAR (30),
username VARCHAR (30)
)
""")


@dp.message(CommandStart()) 
async def start(message: Message):
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (message.from_user.id, message.from_user.full_name, message.from_user.username))
    connection.commit()
    await message.answer(f"Привет {message.from_user.full_name}")


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