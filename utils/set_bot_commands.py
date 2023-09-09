from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni qaytadan ishga tushirish"),
            types.BotCommand("help", "Yordam")
        ]
    )
