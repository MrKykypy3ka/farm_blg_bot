from aiogram import types, Dispatcher


async def echo(message: types.Message):
    await message.answer('/Найти_лекарств')


def register_handlers_others(dp: Dispatcher):
    dp.register_message_handler(echo)