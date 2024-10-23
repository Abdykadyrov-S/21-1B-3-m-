from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.db import get_fruits

start_buttons = [
    [KeyboardButton(text="О нас"), KeyboardButton(text="Товары")]
]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку")


about_inline = [
    [InlineKeyboardButton(text="instagram", url="https://www.instagram.com/"), InlineKeyboardButton(text="telegram", url="https://t.me/Abdykadyrov_S_N")]
]
about_keyboard = InlineKeyboardMarkup(inline_keyboard=about_inline)


product_inline = [
    [InlineKeyboardButton(text="овощи", callback_data="vegetables"), InlineKeyboardButton(text="фрукты", callback_data="fruits")]
]
product_keyboard = InlineKeyboardMarkup(inline_keyboard=product_inline)



fruits = get_fruits()

# fruits = ['apple', 'ananas', 'test']
async def inline_fruits():
    keyboard = InlineKeyboardBuilder()
    for fruit in fruits:
        keyboard.add(InlineKeyboardButton(text=fruit, url="https://t.me/Abdykadyrov_S_N"))
    return keyboard.adjust(2).as_markup()
