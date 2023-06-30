import os
from aiogram import Bot
from aiogram.utils.exceptions import ValidationError
import pytest
import deepl


def test_token_valid():
    token = os.getenv('TOKEN')
    try:
        bot = Bot(token=token)
    except ValidationError:
        pytest.fail('Wrong Telegram Token')


def test_deepl_token():
    api_key = os.getenv('DEEPL_KEY')
    try:
        translator = deepl.Translator(api_key)
        translator.translate_text("Hello World!", target_lang="RU")
    except Exception:
        pytest.fail('Wrong Deepl API key')
