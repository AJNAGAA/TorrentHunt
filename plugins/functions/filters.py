'''Custom filters'''

import re

from pyrogram import filters


class Filter:
    def __init__(self, Client):
        self.Client = Client

    # Filter message from bot admins
    async def admin(self, message):
        return await self.DB.query(
            'fetchval',
            'SELECT EXISTS (SELECT * FROM ADMINS WHERE user_id=$1)',
            message.from_user.id,
        )

    # Command filters with reply keyboard
    def cmd(self, data):
        async def func(flt, Client, message):
            if message.text:
                language = await Client.MISC.user_lang(message)
                text = re.sub('/?', '', message.text)

                if text in [flt.data, self.Client.LG.CMD(flt.data, language)]:
                    return True

        return filters.create(func, data=data)