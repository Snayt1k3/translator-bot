import asyncio

from aiogram import executor, types

from bot import dp
from handlers.main import register_handlers

# Register handlers
register_handlers(dp)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        "Добро пожаловать в бота переводчика! Я здесь, "
        "чтобы помочь вам с переводом текстов на различные языки. "
        "Просто отправьте мне сообщение, которое вы хотите перевести, "
        "и я постараюсь предоставить вам точный и понятный перевод. "
        "Я готов помочь вам преодолеть языковые барьеры и сделать вашу коммуникацию легче и более эффективной. "
        "Не стесняйтесь обращаться ко мне в любое время!"
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True, loop=loop)
