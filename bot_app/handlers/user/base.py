import datetime
import db_methods
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types.voice import Voice
from db_methods import users
from aiogram import types
from bot_app.misc import bot, dp
from bot_app.states.user import User


@dp.message_handler(commands='start', state='*')
async def process_start(message: Message, state: FSMContext):
    user_data = await users.create_user(message.from_user)
    await state.finish()
    await bot.send_message(message.from_user.id,
                           'Привіт! Я Telegram-бот, який допомагає з ефективним використанням часу. \n\n'
                           'Я розшифровую голосові повідомлення та виділяю з них корисну інформацію, '
                           'щоб ви могли швидко і зручно ознайомитися з контентом, не витрачаючи багато'
                           ' часу на прослуховування повідомлень. Якщо у вас є голосове повідомлення, '
                           'яке ви бажаєте розшифрувати, просто перешліть його мені, і я зроблю все решту!')


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def handle_voice_message(message: Message):
    await message.voice.download(destination=f"voice_files/{message.chat.id}_{message.message_id}.oga")
    await db_methods.voice_files.create(message)
    await bot.send_message(message.chat.id, 'Голосове повідомлення отримано та буде оброблено, чекайте')


