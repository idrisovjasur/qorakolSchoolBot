from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

how_subject = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Web Dasturlash', callback_data='web'),
            InlineKeyboardButton(text='Telegram Bot', callback_data='bot')
        ],
        [
            InlineKeyboardButton(text='Robota Texnika', callback_data='robot')
        ],
    ],
)

qora = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text='🔗 Rasmiy kanalga o\'tish uchun link', url='https://t.me/suniy_intelekt_uzb')
        ],
    ],
)
son_maktab = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='330-мактаб', callback_data='330'),
            InlineKeyboardButton(text='131-мактаб', callback_data='131'),
            InlineKeyboardButton(text='165-мактаб', callback_data='165'),

        ],
    ]
)

choice_lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Узбек', callback_data='uz'),
            InlineKeyboardButton(text='Рус', callback_data='ru'),
        ]
    ]
)
