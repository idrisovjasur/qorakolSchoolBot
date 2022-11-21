from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import ADMINS
from loader import dp


@dp.message_handler(commands=['help'],user_id = ADMINS[0])
@dp.message_handler(commands=['help'],user_id = ADMINS[1])
async def help_admin_def(message:types.Message):
    msg = '/start  ---- HAR QANDAY HOLATDAN CHIQISH!\n'
    msg+= '/delete_users ---- BAZA BUTUNLAY TOZALANADI\n\n'
    msg+= '/reklama_text - Matn reklamasi\n'
    msg+='/reklama_photo - Photo reklamasi\n'
    msg+='/reklama_vedio - Vedio reklamasi\n\n'
    msg+='/add_teacher - ustoz qo\'shish\n'
    msg+='/delete_teacher - ustoz o\'chirish\n'
    msg+='/131_users  - BAZA 131\n'
    msg+='/165_users - BAZA 165\n'
    await message.answer(text = msg)
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))