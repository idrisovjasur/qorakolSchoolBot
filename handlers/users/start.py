import datetime
from aiogram import types
from aiogram.dispatcher.filters import Regexp
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from keyboards.default.contact import contact, vaqt, true_false, course, about_teach, ha_yuq, bosh_menu, tugat
from keyboards.inline.url_english import son_maktab, qora, choice_lang, how_subject
from keyboards.inline.url_math import url_math, suniy
from loader import dp, db, bot
from data.config import ADMINS


#####
@dp.message_handler(commands=['start'], state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text="<b>IT School маркази ботига хуш келибсиз!\n</b>", reply_markup=bosh_menu)
    await state.finish()


@dp.message_handler(text='🆒 Rasmiy kanalimiz')
async def kanal_rasmiy(message: types.Message, state: FSMContext):
    await message.answer(text='👇👇👇👇', reply_markup=qora)


@dp.message_handler(text='🔄 Biz haqimizda')
async def about_def_tech_ao(message: types.Message, state: FSMContext):
    await message.answer('Бизнинг Марказимиз ўқтувчилари ҳақида маълумотлар шу йерда!', reply_markup=how_subject)
    await state.set_state('about')


@dp.callback_query_handler(state='about')
async def call_teach_about(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data == 'web':
        dock = 'BQACAgIAAxkBAAMcZPuK_51yMthRA_paiFZ78J77ZFAAAv8-AAIPI9lLoFqjIuikrCkwBA'
        await call.message.answer_document(document=dock, caption='Resume,Web')

    elif call.data == 'bot':
        dock = 'BQACAgIAAxkBAAMcZPuK_51yMthRA_paiFZ78J77ZFAAAv8-AAIPI9lLoFqjIuikrCkwBA'
        await call.message.answer_document(document=dock, caption='Resume,Bot')

    elif call.data == 'robot':
        dock = 'BQACAgIAAxkBAAMcZPuK_51yMthRA_paiFZ78J77ZFAAAv8-AAIPI9lLoFqjIuikrCkwBA'
        await call.message.answer_document(document=dock, caption='Resume,Robota texnika')

    await state.finish()


@dp.message_handler(text='Ortga')
async def ortga_def(message: types.Message):
    await message.answer('Ortga', reply_markup=bosh_menu)


@dp.message_handler(text='📊 165-Maktab statistikasi')
async def statistika(message: types.Message):
    users = db.count_165()
    msg = f"📊 165-Мактаб статистикаси:\n\n"
    msg += f"Рўйҳатдан ўтганлар сони:<b> {users[0]}</b>"
    await message.answer(text=msg)


@dp.message_handler(text='📊 330-Maktab statistikasi')
async def statistika(message: types.Message):
    users = db.count_330()
    msg = f"📊 330-Мактаб статистикаси:\n\n"
    msg += f"Рўйҳатдан ўтганлар сони:<b> {users[0]}</b>"
    await message.answer(text=msg)


@dp.message_handler(text='📊 131-Maktab statistikasi')
async def statistika(message: types.Message):
    users = db.count_131()
    msg = f"📊 131-Мактаб статистикаси:\n\n"
    msg += f"Рўйҳатдан ўтганлар сони:<b> {users[0]}</b>"
    await message.answer(text=msg)


@dp.message_handler(text='✅ Kurslarimizga yozilish')
async def save_def(message: types.Message, state: FSMContext):
    await message.answer("<b>Исмингиз ва Фамилянгизни киритинг!</b>", reply_markup=ReplyKeyboardRemove())
    await state.set_state('ism')


@dp.message_handler(state='ism')
async def ism_def_anceta(message: types.Message, state: FSMContext):
    await message.delete()
    ism = message.text
    await state.update_data(
        {
            'ism': ism
        }
    )
    await message.answer('<b>📱Пастдаги Contact тугмасини босиб,Телефон рақамингизни юборинг</b>', reply_markup=contact)
    await state.set_state('phone')


@dp.message_handler(state='phone', content_types=ContentType.CONTACT)
async def message_phone(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    await message.delete()
    await state.update_data(
        {
            'phone': phone
        }
    )
    await message.answer(text="<b>Отангиз ёки Онангизни ишлайдиган телефон рақамини киритинг</b>\n"
                              "Мисол учун:+998991234567", reply_markup=ReplyKeyboardRemove())

    await state.set_state('home_number')


@dp.message_handler(Regexp('^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'), state='home_number')
async def ona_tel_def_anceta(message: types.Message, state: FSMContext):
    uy_phone = message.text
    await state.update_data(
        {
            'uy_phone': uy_phone
        }
    )

    await message.answer(text='<b>Нечинчи сонли мактабда оқийсиз?</b>', reply_markup=son_maktab)
    await state.set_state('maktab_nomer')


@dp.callback_query_handler(state='maktab_nomer')
async def son_def(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    maktab_soni = call.data
    await state.update_data(
        {
            'maktab_soni': maktab_soni
        }
    )
    await call.message.answer(text="<b>Нечинчи синфда ўқийсиз?</b>")
    await state.set_state('sinf')


@dp.message_handler(state='sinf')
async def sinf_def(message: types.Message, state: FSMContext):
    await message.delete()
    sinf = message.text
    await state.update_data(
        {
            'sinf': sinf
        }
    )
    await message.answer(text='<b>Қайси вақт оралигида мактабга борасиз?</b>', reply_markup=vaqt)
    await state.set_state('vaqt')


@dp.callback_query_handler(state='vaqt')
async def vaqt_def(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    smena = call.data
    await state.update_data(
        {
            'smena': smena
        }
    )
    await call.message.answer(text="<b>Бизнинг IT school дарсларида иштирок етиш истагингиз борми?</b>",
                              reply_markup=true_false)

    await state.set_state('true_false')


@dp.callback_query_handler(state='true_false')
async def true_false_def(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data == '✅ Ha':
        await state.set_state('main')
        await call.message.answer(text="<b>Бизнинг курсларимиздан бирига ёзилинг</b>", reply_markup=course)
    else:
        await call.message.answer('Хайр саломат бyлинг!', reply_markup=bosh_menu)
        await state.finish()
        # await state.reset_state(with_data=False)


@dp.message_handler(state='main')
async def main_def(message: types.Message, state: FSMContext):
    if message.text == '🖥 Web Dasturlash':
        fan1 = 'Web Dasturlash'
        await state.update_data(
            {
                'fan1': fan1
            }
        )
        await message.answer(text='<b>Танланган курсингиз бўйича рўйхатга олиндингиз.\n'
                                  'Тез орада операторлар алоқага чиқишади,\n'
                                  'Биз билан боғланиш: +998993853402,+998994763402</b>')
        await message.answer(text='Яна бирop курсга ёзиласизми?', reply_markup=ha_yuq)

    elif message.text == '💻 Telegram bot':
        fan3 = 'Telegram Bot'
        await state.update_data(
            {
                'fan3': fan3
            }
        )
        await message.answer(text='<b>Танланган курсингиз бўйича рўйхатга олиндингиз.\n'
                                  'Тез орада операторлар алоқага чиқишади,\n'
                                  'Биз билан боғланиш: +998993853402,+998994763402</b>')
        await message.answer(text='Яна бир курсга ёзиласизми?', reply_markup=ha_yuq)

    elif message.text == '🤖 Robota Texnika':
        fan2 = 'Robota Texnika'
        await state.update_data(
            {
                'fan2': fan2
            }
        )
        await message.answer(text='<b>Танланган курсингиз бўйича рўйхатга олиндингиз.\n'
                                  'Тез орада операторлар алоқага чиқишади,\n'
                                  'Биз билан боғланиш: +99899 3853402,+998994763402</b>')
        await message.answer(text='Яна бир курсга ёзиласизми?', reply_markup=ha_yuq)

    elif message.text == '✅ Yes':
        await message.answer('Kurslar!', reply_markup=course)

    elif message.text == '❌ No':
        full_data = await state.get_data()
        name = full_data.get('ism')
        phone = full_data.get('phone')
        uy_phone = full_data.get('uy_phone')
        maktab_soni = int(full_data.get('maktab_soni'))
        sinf = full_data.get('sinf')
        smena = full_data.get('smena')
        fan1 = full_data.get('fan1', '❌')
        fan2 = full_data.get('fan2', '❌')
        fan3 = full_data.get('fan3', '❌')
        global msg
        msg = ''
        msg += f"<b>" \
               f"Исм фамиля:    {name}\n" \
               f"Телефон рақам:   {phone}\n" \
               f"Уйдаги телефон рақам:  {uy_phone}\n" \
               f"Мактаб рақами:   {maktab_soni}\n" \
               f"Синф:   {sinf}\n" \
               f"Смена:  {smena}\n" \
               f"фан1:  {fan1}\n" \
               f"фан2:   {fan2}\n" \
               f"фан3:   {fan3}</b>"
        await message.answer('Сиз юборган маълумотлар ҳаммаси тўғрими\n\n------------\n' + msg, reply_markup=tugat)
        try:
            db.add_user(
                id=message.from_user.id,
                name=name,
                maktab_raqami=maktab_soni,
                phone=uy_phone
            )
        except Exception as e:
            pass

    elif message.text == '✅ Ha':
        await message.answer("Маълумотлар операторга юборилди!", reply_markup=bosh_menu)
        await bot.send_message(chat_id=ADMINS[0],
                               text=f'{message.from_user.id} id ga ega bo\'lgan foydalanuvchi\n--------\n' + msg + f"\n\n@{message.from_user.username} dan yangi xabar!")
        await bot.send_message(chat_id=ADMINS[1],
                               text=f'{message.from_user.id} id ga ega bo\'lgan foydalanuvchi\n--------\n' + msg + f"\n\n@{message.from_user.username} dan yangi xabar!")
        await state.finish()

    elif message.text == '❌ Yuq':
        await message.answer('Рўйхатдан ўтишни бошидан бошланг', reply_markup=bosh_menu)
        await state.finish()

# dp.callback_query_handler()


# @dp.message_handler(content_types=ContentType.DOCUMENT)
# async def jjj(message: types.Message):
#     f = message.document.file_id
#     await message.answer(f)
