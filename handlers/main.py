import os

from aiogram import Dispatcher, types
import deepl


async def EchoTranslate(msg: types.Message):
    translator = deepl.Translator(os.getenv('DEEPL_KEY'))
    result = translator.translate_text(msg.text, target_lang="RU")
    await msg.answer(result.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(EchoTranslate, lambda msg: '/' not in msg.text)
