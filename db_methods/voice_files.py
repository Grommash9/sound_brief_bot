import datetime
from aiogram.types import Message
from db_methods.base import create_dict_con, sync_create_con
from db_methods.models import VoiceFile

async def create(message: Message):
    con, cur = await create_dict_con()
    await cur.execute('insert ignore into voice_files (chat_id, message_id) '
                      'values (%s, %s)',
                      (message.chat.id, message.message_id))
    await con.commit()
    await con.ensure_closed()


def update_text(new_text, chat_id, message_id):
    con, cur = sync_create_con()
    cur.execute('update voice_files set text = %s '
                'where chat_id = %s '
                'and message_id = %s ',
                (new_text, chat_id, message_id))
    con.commit()
    con.close()


def get_all_to_make_short():
    con, cur = sync_create_con()
    cur.execute('select record_id from voice_files where text is not NUll and short_text is NULL ')
    record_ids_data_list = cur.fetchall()
    con.close()
    return [voice_file[0] for voice_file in record_ids_data_list]


def get_text(record_id):
    con, cur = sync_create_con()
    cur.execute('select text from voice_files where record_id = %s', (record_id,))
    text_data = cur.fetchone()
    con.close()
    return text_data[0]


def get(record_id) -> VoiceFile:
    con, cur = sync_create_con()
    cur.execute('select record_id, chat_id, message_id, short_text, text from voice_files where record_id = %s', (record_id,))
    voice_file_data = cur.fetchone()
    con.close()
    return VoiceFile(*voice_file_data)


def update_short_text(short_text, voice_file_id):
    con, cur = sync_create_con()
    cur.execute('update voice_files set short_text = %s where record_id = %s ', (short_text, voice_file_id))
    con.commit()
    con.close()


def get_info_for_send() -> list[int]:
    con, cur = sync_create_con()
    cur.execute('select record_id from voice_files where short_text is not Null and sent is NULL ')
    record_ids_data_list = cur.fetchall()
    con.close()
    return [voice_file[0] for voice_file in record_ids_data_list]


def update_as_sent(voice_file_id):
    con, cur = sync_create_con()
    cur.execute('update voice_files set sent = %s where record_id = %s',
                (datetime.datetime.now(), voice_file_id))
    con.commit()
    con.close()
