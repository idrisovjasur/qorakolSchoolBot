from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

how_subject = InlineKeyboardMarkup(
    inline_keyboard=[
        [
             InlineKeyboardButton(text = 'Ingliz tili',callback_data='ingliz'),
             InlineKeyboardButton(text = 'IT',callback_data='it')
        ],
        [
             InlineKeyboardButton(text = 'Math',callback_data='math')
        ],
    ],
)

qora = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text = '🔗 Rasmiy kanalga o\'tish uchun link',url='https://t.me/qora_kol')
        ],
    ],
)

son_maktab = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='131-мактаб',callback_data='131'),
            InlineKeyboardButton(text = '165-мактаб',callback_data='165'),
        ],
    ]
)

choice_lang = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'Узбек',callback_data='uz'),
            InlineKeyboardButton(text = 'Рус',callback_data='ru'),
        ]
    ]
)