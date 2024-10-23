from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from app.keyboards import start_keyboard, about_keyboard, product_keyboard, inline_fruits

router = Router()

@router.message(CommandStart()) 
async def start(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}", reply_markup=start_keyboard)

@router.message(Command('help'))
async def help_comm(message: types.Message):
    await message.reply('Чем могу помочь?')

@router.message(F.text == "О нас")
async def help_comm(message: types.Message):
    await message.answer("""Компания Sulpak – крупнейшая торговая компания Казахстана, лидер в реализации электроники и бытовой техники.""", reply_markup=about_keyboard)

@router.message(F.text == "Товары")
async def help_comm(message: types.Message):
    await message.answer("Выберите категорию товара", reply_markup=product_keyboard)

@router.callback_query(F.data == "vegetables")
async def inline_vegetables(callback: types.CallbackQuery):
    await callback.answer("Овощи", show_alert=True)
    await callback.message.answer("Овощи")

@router.callback_query(F.data == "fruits")
async def inline_fruit(callback: types.CallbackQuery):
    # await callback.answer("Фрукты")
    await callback.message.edit_text("Фрукты", reply_markup=await inline_fruits())

@router.message()
async def echo(message: types.Message):
    await message.answer("Я вас не понял")