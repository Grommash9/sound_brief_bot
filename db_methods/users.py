import datetime

from aiogram.types import User

from db_methods.base import create_dict_con


async def create_user(user: User):
    con, cur = await create_dict_con()
    await cur.execute('insert ignore into data_tg_user (user_id, `name`, user_name) '
                      'values (%s, %s, %s)',
                      (user.id, user.first_name, user.username))
    await con.commit()
    await con.ensure_closed()

