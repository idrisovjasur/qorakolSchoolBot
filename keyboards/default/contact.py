from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱 Contact', request_contact=True),
        ],
    ], resize_keyboard=True,
)
vaqt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='(8:00-12:00)', callback_data='(8:00-12:00)'),
            InlineKeyboardButton(text='(13:00-17:00)', callback_data='(13:00-17:00)')
        ],
    ], resize_keyboard=True
)

true_false = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Ha', callback_data='✅ Ha'),
            InlineKeyboardButton(text='❌ Yo\'q', callback_data='❌ Yo\'q')
        ],
    ]

)

course = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🖥 Web Dasturlash'),
            KeyboardButton(text='💻 Telegram bot')
        ],
        [
            KeyboardButton(text='🤖 Robota Texnika')
        ],
    ], resize_keyboard=True
)

about_teach = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ingliz tili o\'qtuvchisi haqida', callback_data='english'),
            InlineKeyboardButton(text='Matematika o\'qtuvchisi haqida', callback_data='math'),
        ],
        [
            InlineKeyboardButton(text='IT o\'qtuvchisi haqida', callback_data='it'),
        ],
        [
            InlineKeyboardButton(text='Ortga', callback_data='back'),
        ]
    ]
)

ha_yuq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Yes'),
            KeyboardButton(text='❌ No')
        ],
    ], resize_keyboard=True
)

tugat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Ha'),
            KeyboardButton(text='❌ Yuq')
        ],
    ], resize_keyboard=True
)

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📊 330-Maktab statistikasi'),
            KeyboardButton(text='✅ Kurslarimizga yozilish'),

        ],
        [
            KeyboardButton(text='📊 165-Maktab statistikasi'),
            KeyboardButton(text='🔄 Biz haqimizda')
        ],
        [
            KeyboardButton(text='📊 131-Maktab statistikasi'),
            KeyboardButton(text='🆒 Rasmiy kanalimiz')

        ]

    ],
    resize_keyboard=True
)
