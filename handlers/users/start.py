import datetime
from aiogram import types
from aiogram.dispatcher.filters import Regexp
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from keyboards.default.contact import contact, vaqt, true_false, course, about_teach, ha_yuq, bosh_menu
from keyboards.inline.url_english import url_english
from keyboards.inline.url_math import url_math, suniy
from loader import dp, db, bot
from data.config import ADMINS

@dp.message_handler(commands=['update_english'],user_id = ADMINS)
async def update_english_def(message:types.Message,state:FSMContext):
    await message.answer('Ustoz ismi:')
    await state.set_state('en_ism')
@dp.message_handler(state='en_ism')
async def ism_in_def(message:types.Message,state:FSMContext):
    en_ism = message.text
    await state.update_data(
        {
            'en_ism':en_ism
        }
    )
    await message.answer('Ustoz familyasi:')
    await state.set_state('en_familya')
@dp.message_handler(state='en_familya')
async def familya_in_def(message:types.Message,state:FSMContext):
    familya = message.text
    await state.update_data(
        {
            'familya_en':familya
        }
    )
    await message.answer('IELTS score:')
    await state.set_state('ielts')
@dp.message_handler(state='ielts')
async def ielts_in_def(message:types.Message,state:FSMContext):
    ieltss = message.text
    await state.update_data(
        {
            'ieltss':ieltss
        }
    )
    await message.answer('Stage:')
    await state.set_state('stage')
@dp.message_handler(state='stage')
async def stage_in_def(message:types.Message,state:FSMContext):
    stages = message.text
    await state.update_data(
        {
            'stages':stages
        }
    )

    await message.answer('Malumot saqlandi!',reply_markup=bosh_menu)
    await state.reset_state(with_data=False)

@dp.message_handler(commands=['update_matematika'],user_id = ADMINS)
async def update_mat_def(message:types.Message,state:FSMContext):
    await message.answer('Ustoz ismi:')
    await state.set_state('mat_ism')
@dp.message_handler(state='mat_ism')
async def ism_in_def(message:types.Message,state:FSMContext):
    mat_ism = message.text
    await state.update_data(
        {
            'mat_ism':mat_ism
        }
    )
    await message.answer('Ustoz familyasi')
    await state.set_state('mat_familya')
@dp.message_handler(state='mat_familya')
async def familya_mat_def(message:types.Message,state:FSMContext):
    mat_fam = message.text
    await state.update_data(
        {
            'mat_fam':mat_fam
        }
    )
    await message.answer('Stage:')
    await state.set_state('mat_st')
@dp.message_handler(state='mat_st')
async def mat_stage_def(message:types.Message,state:FSMContext):
    mat_st = message.text
    await state.update_data(
        {
            'mat_st':mat_st
        }
    )

    await message.answer('Malumot saqlandi!',reply_markup=bosh_menu)
    await state.reset_state(with_data=False)



@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message,state:FSMContext):

    await message.answer(f"<b>Salom, {message.from_user.full_name}!\n"
                         f"Qorakul o'quv markaz rasmiy botiga xush kelibsiz ✅\n</b>",reply_markup=bosh_menu)


@dp.message_handler(text='🔄 Biz haqimizda')
async def about_def_tech_ao(message:types.Message,state:FSMContext):
    await message.answer('About!',reply_markup=about_teach)

@dp.message_handler(text='Ingliz tili o\'qtuvchisi haqida')
async def teach_def1(message:types.Message,state:FSMContext):
    if message.text=='Ingliz tili o\'qtuvchisi haqida':
        data = await state.get_data()
        ism = data.get('en_ism')
        fam = data.get('familya_en')
        iel = data.get('ieltss')
        st = data.get('stages')
        await message.answer_photo('AgACAgIAAxkBAAIBzWNMiEBF4VX-AasUP0VX1UHo-EXhAAJ-vDEbCN1oSqoh61XXc8QnAQADAgADeAADKgQ',
                                   caption=f"<b>O'qtuvchi haqida ma'lumot,\n"
                                           f"Ism: {ism}\n"
                                           f"Familya: {fam}\n"
                                           f"IELTS: {iel}\n"
                                           f"Stage: {st}\n"
                                           f"----------------\n"
                                           f"Har bir daraja 3 oy vaqtni oladi, Bizda 6 ta daraja bo’lib,4-darajani tugatib siz IELTS uchun harakat qilaversangiz buladi\n"
                                           f"Nima uchun Ingliz tilini urganish kerak:</b>",reply_markup=url_english)


@dp.message_handler(text='IT o\'qtuvchisi haqida')
async def itteach_def_teach(message:types.Message,state:FSMContext):
    data = await state.get_data()
    mat_ism = data.get('mat_ism')
    mat_fam = data.get('mat_fam')
    mat_st = data.get('mat_st')
    await message.answer_photo('AgACAgIAAxkBAAIH4GNORPDBNdvb5APE6pUhF0PVeESTAAKfwTEbGIRxSvQP-Z9t8ny1AQADAgADeQADKgQ',
                               caption=f"Ism: {mat_ism}\n"
                                       f"Familya: {mat_fam}\n"
                                       f"Stage: {mat_st}\n"
                                       f"----------------\n"
                                       f"<b>IT — ingliz tilidan olingan «Information Technology» so‘zlarining qisqartmasi bo‘lib, o‘zbek tilida «Axborot texnologiyalari» deb yuritiladi. \n"
                                       f"Shunday bo‘lsa ham, biz bu so‘zni IT ko‘rinishida talaffuz qilamiz va ishlatamiz.\n"
                                       f"IT sizdan kup vaqt sariflashingizni talab qiladi:\n"
                                       f"Qancha vaqtda urgansa buladi ?  Bu javobga xichkim anniq javob bera olmaydi….\n"
                                       f"Chunki bu IT sohasi endi biznig mamlakatimizda o’sa boshladi… Biz O’zbekiston uchun ko’p IT soxalari bor va Biz daris davomida dunyoga mashxur bulgan PYTHON dasturlash tilini o’rgnamiz.\n"
                                       f"Ko’rs davomiyligi 9 oy buladi va yana 3 oy real project qilamiz:</b>", reply_markup=suniy)


@dp.message_handler(text='Matematika o\'qtuvchisi haqida')
async def matem_def_teach(message:types.Message,state:FSMContext):
        data = await state.get_data()
        mat_ism = data.get('mat_ism')
        mat_fam = data.get('mat_fam')
        mat_st = data.get('mat_st')
        await message.answer_photo('AgACAgIAAxkBAAIC72NM9BFPYF_pyJBk-tvqP_6KAijQAALbvDEbCN1oSuCQsqzVIpGZAQADAgADeQADKgQ',
                                   caption=f"Ism: {mat_ism}\n"
                                           f"Familya: {mat_fam}\n"
                                           f"Stage: {mat_st}\n"
                                           f"----------------\n"
                                           f"<b>Matimatika darajani O’rganish uchun qancha vaqt kerak? Matematikani birinchi urinda oxiri yuq……...\n"
                                           f"Lekin siz uchun Unversit, Prizident maktab va SAT  uchun eng kamida puxta va qattiq o'rganish orqali 1 yil kerak buladi.\n"
                                           f"Nima uchun Matematika tilini urganish kerak:</b>",reply_markup=url_math)
@dp.message_handler(text='Ortga')
async def ortga(message:types.Message):
        await message.answer('Ortga',reply_markup=bosh_menu)


@dp.message_handler(text='📊 Statistika')
async def statistika(message:types.Message):
    all_user = db.count_users()[0]
    data = datetime.datetime.today()
    msg = f"<b>👥 Botdagi obunachilar:  {all_user} ta</b>\n"
    msg+=f"<b>🕖Bugungi sana: {data}</b>\n\n"
    msg+=f"<b>📊 Bot statistikasi</b>"
    await message.answer(msg,reply_markup=bosh_menu)


@dp.message_handler(text='✅ Kursga yozilish')
async def save_def(message:types.Message,state:FSMContext):
    await message.answer("<b>Ismingiz va Familyangizni kiriting!</b>",reply_markup=ReplyKeyboardRemove())
    await state.set_state('ism')
@dp.message_handler(state='ism')
async def ism_def_anceta(message:types.Message,state:FSMContext):
    ism = message.text
    await state.update_data(
        {
            'ism':ism
        }
    )
    await message.answer('<b>📱 Telefon reqamingizni yuboring! Misol uchun:+998991234567</b>',reply_markup=contact)
    await state.set_state('phone')
@dp.message_handler(state='phone',)
async def message_phone(message:types.Message,state:FSMContext):
    phone = message.text
    await state.update_data(
        {
            'phone':phone
        }
    )
    await message.answer(text="<b>Uyingizdagilarni (ota/ona) ishlaydigan telefon raqamini kiriting</b>\n"
                         "Misol uchun:+998991234567",reply_markup=ReplyKeyboardRemove())
    await state.set_state('home_number')
@dp.message_handler(state='phone',content_types=ContentType.CONTACT)
async def phone_def_anceta(message:types.Message,state:FSMContext):
    phone = message.contact.phone_number
    await state.update_data(
        {
            'phone':phone
        }
    )
    await message.answer(text="<b>Uyingizdagilarni (ota/ona) ishlaydigan telefon raqamini kiriting</b>\n"
                         "Misol uchun:+998991234567",reply_markup=ReplyKeyboardRemove())
    await state.set_state('home_number')
@dp.message_handler(Regexp('^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'),state='home_number')
async def ona_tel_def_anceta(message:types.Message,state:FSMContext):
    uy_phone = message.text
    await state.update_data(
        {
            'uy_phone':uy_phone
        }
    )
    try:
        data = await state.get_data()
        ism = data.get('ism')
        db.add_user(
            id=message.from_user.id,
            name=ism,
            phone=uy_phone,
        )
    except:
        pass
    await message.answer(text='<b>Nechinchi sonli maktabda o\'qiysiz?</b>')
    await state.set_state('maktab_nomer')
@dp.message_handler(state='home_number')
async def bug_number(message:types.Message,state:FSMContext):
    await message.answer('<b>Telefon raqamni to\'g\'ri kiriting!</b>')
    await state.set_state('home_number')

@dp.message_handler(state='maktab_nomer')
async def son_def(message:types.Message,state:FSMContext):
    maktab_soni = message.text
    await state.update_data(
        {
            'maktab_soni':maktab_soni
        }
    )
    await message.answer(text="<b>Nechinchi sinfda o'qiysiz?</b>")
    await state.set_state('sinf')

@dp.message_handler(state='sinf')
async def sinf_def(message:types.Message,state:FSMContext):
    sinf = message.text
    await state.update_data(
        {
            'sinf':sinf
        }
    )
    await message.answer(text='<b>Qaysi vaqt oralig\'ida maktabga borasiz?</b>',reply_markup=vaqt)
    await state.set_state('vaqt')

@dp.message_handler(state='vaqt')
async def vaqt_def(message:types.Message,state:FSMContext):
    smena = message.text
    await state.update_data(
        {
            'smena':smena
        }
    )
    await message.answer(text="<b>DIQQAT⁉️\n"
                              "Agarda,sizning maktabingizga bizning o'quv markazimiz filiali joylashsa,\n"
                              "siz o'zingiz qiziqqan fanga qatnashasizmi?</b>",reply_markup=true_false)

    await state.set_state('true_false')

@dp.message_handler(state='true_false')
async def true_false_def(message:types.Message,state:FSMContext):
    if message.text=='✅ Ha':
        await state.set_state('main')
        await message.answer(text="<b>Bizning kurslarimizdan biriga yoziling</b>",reply_markup=course)
    else:
        await message.answer('Xayr salomat bo\'ling!')
        await message.answer('Qayta ishga tushirish uchun /start buyrig\'ini bosing va qaytadan ma\'lumot kiriting!',reply_markup=ReplyKeyboardRemove())
        await state.reset_state(with_data=False)





@dp.message_handler(state='main')
async def main_def(message:types.Message,state:FSMContext):
    if message.text=='📓 Matematika':
        fan1 = 'Matematika'
        await state.update_data(
            {
                'fan1':fan1
            }
        )
        await message.answer_photo('AgACAgIAAxkBAAPTY0x00bCVKwiQyUo8s-eolsCX8ioAAlu_MRuvtWhKtyaaf1Db1G4BAAMCAANtAAMqBA',
                                   caption='<b>Tanlangan kursingiz bo\'yicha ro\'yxatga olindingiz,\n'
                                  'tez orada operatorlar aloqaga chiqishadi.\n'
                                           'Biz bilan bog\'lanish:+99899 719 14 07</b>')
        await message.answer(text='Yana bir kursga yozilasizmi?',reply_markup=true_false)
    elif message.text == '💻 IT':
        fan3 = 'IT'
        await state.update_data(
            {
                'fan3':fan3
            }
        )
        await message.answer_photo('AgACAgIAAxkBAAIBmGNMhHfzn4eghSWeV255Q_FyQCLcAAJsvzEbr7VoSmO8YcGj88RPAQADAgADbQADKgQ',
        caption='<b>Tanlangan kursingiz bo\'yicha ro\'yxatga olindingiz,\n'
                                  'tez orada operatorlar aloqaga chiqishadi.\n'
                                  'Biz bilan bog\'lanish:+99899 719 14 07</b>')
        await message.answer(text='Yana bir kursga yozilasizmi?',reply_markup=true_false)

    elif message.text=='🇺🇸 Ingliz tili':
        fan2 = 'Ingliz tili'
        await state.update_data(
            {
                'fan2':fan2
            }
        )
        await message.answer_photo('AgACAgIAAxkBAAPVY0x2jjGWgog-f3FwRWd97IBf99sAAmC_MRuvtWhKp19kE0lw3FUBAAMCAANtAAMqBA',
                                   caption='<b>Rahmat,tanlangan kursingiz bo\'yicha ro\'yxatga olindingiz,\n'
                                  'tez orada operatorlar aloqaga chiqishadi.\n'
                                           'Biz bilan bog\'lanish:+99899 719 14 07</b>')
        await message.answer(text='Yana bir kursga yozilasizmi?',reply_markup=true_false)

    elif message.text=='✅ Ha':
        await message.answer('Kurslar!',reply_markup=course)

    elif message.text=='❌ Yo\'q':
        # await message.answer(text='Bosh Menyu',reply_markup=course)
        # await message.answer("Xabarlaringiz adminga yuborildi✅ ")
        full_data = await state.get_data()
        name = full_data.get('ism')
        phone = full_data.get('phone')
        uy_phone = full_data.get('uy_phone')
        maktab_soni = full_data.get('maktab_soni')
        sinf = full_data.get('sinf')
        smena = full_data.get('smena')
        fan1 = full_data.get('fan1')
        fan2 = full_data.get('fan2')
        fan3 = full_data.get('fan3')
        global msg
        msg=''
        msg += f"<b>"\
                             f"Ism familyangiz:   {name}\n"\
                             f"Telefon raqamingiz:   {phone}\n"\
                             f"Uydagi telefon raqam:  {uy_phone}\n"\
                             f"Maktab raqami:   {maktab_soni}\n"\
                             f"Sinf:   {sinf}\n"\
                             f"Smena:  {smena}\n"\
                             f"fan1:   {fan1}\n"\
                             f"fan2:   {fan2}\n"\
                             f"fan3:   {fan3}</b>"
        await message.answer('Siz yuborgan malumotlar hammasi tog\'rimi\n--------------\n'+msg,reply_markup=ha_yuq)

    elif message.text=='✅Yes':
        await message.answer("Ma'lumotlar adminga yuborildi!",reply_markup=bosh_menu)
        await bot.send_message(chat_id=ADMINS[0],text=f'{message.from_user.id} id ga ega bo\'lgan foydalanuvchi\n--------\n'+msg+f"\n\n@{message.from_user.username} dan yangi xabar!")
        await state.finish()
    elif message.text=='❌No':
        await message.answer('Qayta ishga tushirish uchun /start buyrig\'ini bosing va qaytadan ma\'lumot kiriting!',reply_markup=ReplyKeyboardRemove())
        await state.finish()









@dp.message_handler(content_types=ContentType.PHOTO)
async def jjj(message:types.Message):
    f = message.photo[-1].file_id
    await message.answer(f)

"""
from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.contact import contact,db_save
from keyboards.inline.menu_keyboard import menu_keyboard
from loader import dp,db

@dp.message_handler(CommandStart())
@dp.message_handler(text = '❌ Yo\'q')
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer("Hurmatli Foydalanuvchi,Ro'yxatdan o'ting!")
    await message.answer("Ismingiz va Familyangizni kiriting!")
    await state.set_state('ism')
@dp.message_handler(state='ism')
async def ism(message:types.Message,state:FSMContext):
    ism = message.text
    await state.update_data(
        {
            'ism':ism
        }
    )
    await message.answer('Telefon Raqamni yuboring!',reply_markup=contact)
    await state.set_state('phone')
@dp.message_handler(state='phone',content_types=ContentType.CONTACT)
async def phone(message:types.Message,state:FSMContext):
    global ism,phone
    phone = message.contact.phone_number
    await state.update_data(
        {
            'phone':phone
        }
    )
    data = await state.get_data()
    ism = data.get('ism')
    phone = data.get('phone')
    msg = 'Siz Kiritgan ma\'lumotlar:\n'
    msg+=f"Ism:{ism}\n"
    msg+=f"Tel raqam:{phone}\n\n"
    msg+=f"<b>Ma'lumtlar to'grimi?</b>"
    await state.finish()
    await message.answer(text = msg,reply_markup=db_save)
@dp.message_handler(text = '✅ Ha')
async def save_sql_user(message:types.Message):
        try:
            db.add_user(
            id=message.from_user.id,
            name=ism,
            phone=phone
        )
            await message.answer(text="<b>Ma'lumotlar qabul qilindi!</b>",reply_markup=ReplyKeyboardRemove())
            file = 'AgACAgIAAxkBAAMGY0fdyvv6wRh38dwUb-d7rVIsgkgAAhe_MRtq7UFKMkTluaJtoHEBAAMCAAN5AAMqBA'
            await message.answer_photo(file, caption='<b>Yetkazib berish bo\'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi.</b>',reply_markup=menu_keyboard)

        except:
            file = 'AgACAgIAAxkBAAMGY0fdyvv6wRh38dwUb-d7rVIsgkgAAhe_MRtq7UFKMkTluaJtoHEBAAMCAAN5AAMqBA'
            await message.answer(text="<b>Siz allaqachon Ro'yhatdan o'tgansiz!</b>",reply_markup=ReplyKeyboardRemove())
            await message.answer_photo(file, caption='<b>Yetkazib berish bo\'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi.</b>',reply_markup=menu_keyboard)

@dp.message_handler(content_types=ContentType.PHOTO)
async def phone(message:types.Message,state:FSMContext):
    await message.answer(text=message.photo[-1].file_id)
"""