import asyncio
from aiogram.types import Message, ContentType,ReplyKeyboardRemove
from data.config import ADMINS
from aiogram.dispatcher import FSMContext

from keyboards.default.contact import true_false
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

@dp.message_handler(text = '/all_users',user_id=ADMINS[0])
async def all_user_def(message:Message,state:FSMContext):
    users = db.select_all_users()
    a = []
    for i in users:
        a.append(f'Ism:{i[1]}\n'
                 f'Tel:{i[2]}')
    for j in a:
        await message.answer(j)

@dp.message_handler(text = '/delete_users',user_id = ADMINS[0])
async def delete_user_def(message:Message,state:FSMContext):
    await message.answer('DIQQAT!\n'
                         'Hamma foydalanuvchi bazadan o\'chadi!',reply_markup=true_false)
    await state.set_state('delete_user')

@dp.message_handler(state='delete_user')
async def delete_user_state_def(message:Message,state:FSMContext):
    if message.text=='✅ Ha':
          db.delete_users()
          await message.answer("Hamma Foydalanuvchi bazadan o'chirildi ✅",reply_markup=ReplyKeyboardRemove())
          await state.finish()
    else:
        await message.answer('Bazada foydalanuvchilar o\'chirilmadi',reply_markup=ReplyKeyboardRemove())
        await state.finish()

