import asyncio 
import logging
import sqlite3

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)

from config import token

bot = Bot(token=token)
dp = Dispatcher()

connection = sqlite3.connect("users.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS  users (
id INTEGER,
full_name VARCHAR (30),
age VARCHAR (30),
phone_number VARCHAR (30)
)
""")

class Register(StatesGroup):
    full_name = State()
    age = State()
    number = State()


data_inline = [
    [InlineKeyboardButton(text="нет ❌", callback_data="not"), InlineKeyboardButton(text="да ✅", callback_data="yes")]
]
data_keyboard = InlineKeyboardMarkup(inline_keyboard=data_inline)


register_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Зарегистрироваться 📋")]], one_time_keyboard=True, resize_keyboard=True)

@dp.message(CommandStart()) 
async def start(message: Message):
    await message.answer(f"Привет {message.from_user.full_name}", reply_markup=register_keyboard)

@dp.message(F.text == "Зарегистрироваться 📋")
async def register_1(message: Message, state: FSMContext):
    await message.answer("Введите ФИО ")
    await state.set_state(Register.full_name)

@dp.message(Register.full_name)
async def register_2(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Введите возраст")
    await state.set_state(Register.age)

@dp.message(Register.age)
async def register_3(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите номер телефона")
    await state.set_state(Register.number)

@dp.message(Register.number)
async def register_4(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    full_name = data['full_name']    
    age = data['age']    
    number = data['number']
    await message.answer(f"""Верны ли ваши данные?:
                        ФИО - {full_name}
                        Возраст - {age}
                        Номер телефона - {number}
                         """, reply_markup=data_keyboard)

@dp.callback_query(F.data == "yes")
async def register_yes(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    full_name = data['full_name']    
    age = data['age']    
    number = data['number']
    cursor.execute(f"INSERT INTO users VALUES (?,?,?,?)", (callback.message.from_user.id, full_name, age, number))
    connection.commit()
    await callback.answer("Ваши данные сохранены")
    await callback.message.edit_text("Вы успешно прошли регистрацию")
    await state.clear()


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