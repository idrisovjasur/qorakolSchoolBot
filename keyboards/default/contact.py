from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱 Contact',request_contact=True),
        ],
    ],resize_keyboard=True,
)
vaqt = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='(8:00-12:00)'),
            KeyboardButton(text='(13:00-17:00)')
        ],
    ],resize_keyboard=True
)

true_false = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Ha'),
            KeyboardButton(text='❌ Yo\'q')
        ],
    ],resize_keyboard=True
)

course = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📓 Matematika'),
            KeyboardButton(text='🇺🇸 Ingliz tili')
        ],
        [
            KeyboardButton(text='💻 IT')
        ],
    ],resize_keyboard=True
)

about_teach = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ingliz tili o\'qtuvchisi haqida'),
            KeyboardButton(text='Matematika o\'qtuvchisi haqida'),
        ],
        [
            KeyboardButton(text='IT o\'qtuvchisi haqida'),
        ],
        [
            KeyboardButton(text='Ortga'),
        ]
    ],resize_keyboard=True
)

ha_yuq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅Yes'),
            KeyboardButton(text='❌No')
        ],
    ],resize_keyboard=True
)

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Kursga yozilish'),
            KeyboardButton(text='🆒 Rasmiy kanal',),

        ],
        [
            KeyboardButton(text='🔄 Biz haqimizda'),
            KeyboardButton(text='📊 Statistika')

        ],
    ],resize_keyboard=True
)