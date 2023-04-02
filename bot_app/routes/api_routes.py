import os
import pathlib

import db_methods.voice_files
from bot_app import config
from aiohttp import web

from bot_app.misc import routes, bot


@routes.get(f'/{config.ROUTE_URL}/send_message')
async def get_handler(request):
    tx_data = dict(request.query)
    voice_file_id = tx_data['voice_file_id']

    voice_file = db_methods.voice_files.get(voice_file_id)


    try:
        await bot.send_message(voice_file.chat_id, voice_file.short_text,
                               reply_to_message_id=voice_file.message_id)
    except Exception as e:
        return web.Response(status=404, body=str(e))
    return web.Response(status=200, body='ok')

