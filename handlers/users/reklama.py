import asyncio
from aiogram.types import Message, ContentType
from data.config import ADMINS
from aiogram.dispatcher import FSMContext

from keyboards.inline.url_english import qora
from loader import db,dp,bot


@dp.message_handler(text='/reklama_text',user_id=ADMINS[0])
async def reklama_text_def(message:Message,state:FSMContext):
    await message.answer("reklama matnini kiriting!")
    await state.set_state('reklama_text')

@dp.message_handler(state='reklama_text')
async def reklama_def_dtat(message:Message,state:FSMContext):
    text = message.text
    users = db.select_all_users()
    await state.finish()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id,text=text)
        await asyncio.sleep(0.05)
    await message.answer("Reklama hammaga yuborildi")


####RASM
@dp.message_handler(text='/reklama_photo',user_id =ADMINS[0])
async def reklama_photo_def(message:Message,state:FSMContext):
      await message.answer('Reklama Photo rasmini yuboring')
      await state.set_state('reklama_photo')

@dp.message_handler(state='reklama_photo',content_types=ContentType.PHOTO)
async def state_photo_defaa_data(message:Message,state:FSMContext):
       global photo_id
       photo_id=message.photo[-1].file_id
       await message.answer('Caption yuboring!')
       await state.set_state('caption')

@dp.message_handler(state='caption')
async def caption_def(message:Message, state:FSMContext):
           caption = message.text
           users = db.select_all_users()
           await state.finish()
           for user in users:
             user_id = user[0]
             await bot.send_photo(chat_id=user_id,photo=photo_id,caption=caption)
             await asyncio.sleep(0.05)

           await message.answer('reklama yuborildi hammaga')


@dp.message_handler(text='/reklama_video',user_id=ADMINS[0])
async def video_def_statelar_bilan(message:Message,state:FSMContext):
    await message.answer('Reklama Video ni yuboring')
    await state.set_state('reklama_video')

@dp.message_handler(state='reklama_video',content_types=ContentType.VIDEO)
async def video_reklama_def(message:Message,state:FSMContext):
    global video_id
    video_id=message.video.file_id
    await message.answer('Caption yuboring')
    await state.set_state('caption_video')

@dp.message_handler(state='caption_video')
async def caption_video(message:Message,state:FSMContext):
    caption = message.text
    users = db.select_all_users()
    await state.finish()
    for user in users:
        user_id = user[0]
        await bot.send_video(chat_id=user_id,video=video_id,caption=caption)
        await asyncio.sleep(0.05)

    await message.answer('reklama hammaga yuborildi')

@dp.message_handler(text='🆒 Rasmiy kanal')
async def resimiy_kanal(message:Message):
    id = 'AgACAgIAAxkBAAIHwGNNrDSpSsog-ruh7NReUfpbmz6FAAK2wjEbbFZoSvs8xjavhGNRAQADAgADeQADKgQ'
    await message.answer_photo(photo=id,reply_markup=qora)
