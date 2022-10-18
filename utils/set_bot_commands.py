from aiogram import types




async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand('reklama_text',"Matn reklamasi"),
            types.BotCommand('reklama_photo', "Photo reklamasi"),
            types.BotCommand('reklama_vedio', "Vedio reklamasi"),
        ]
    )
