from aiogram import Dispatcher, types


async def EchoTranslate(msg: types.Message):
    pass


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(EchoTranslate)
