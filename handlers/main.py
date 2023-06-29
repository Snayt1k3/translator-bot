import os
from database.database import DataBase
from aiogram import Dispatcher, types
import deepl


async def EchoTranslate(msg: types.Message):
    translator = deepl.Translator(os.getenv('DEEPL_KEY'))
    result = translator.translate_text(msg.text, target_lang="RU")

    # save msg for view user msg history
    await DataBase.InsertOne(
        'message_history',
        {
            'user_id': msg.from_user.id,
            'msg': msg.text,
            'translated_msg': result.text
        })

    await msg.answer(result.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(EchoTranslate, lambda msg: '/' not in msg.text)
