# meta developer: @amoremods | edit by: @babycodera

# meta editor : @babycodera

# meta pic: https://te.legra.ph/file/0251f5d602a8f32cd7368.png

# meta banner: https://raw.githubusercontent.com/AmoreForever/assets/master/Instsave.jpg

__version__ = (1, 0, 0)

from .. import utils, loader

chat = "@amoreconverterbot"

class CreativeMod(loader.Module):

    """create creative image"""

    strings = {

        "name": "draft",

        "processing": (

            "<emoji document_id='6318766236746384900'>🕔</emoji> <b>Kuting...</b>"

        ),

        "mods": (

            "<a href='https://t.me/amoreconverterbot'>Tayyor</a>"

        ),

    }

    @loader.group_member

    @loader.command(ru_doc="text")

    async def draftcmd(self, message):

        """creative image"""

        text = utils.get_args_raw(message)

        message = await utils.answer(message, self.strings("processing"))

        async with self._client.conversation(chat) as conv:

            msgs = []

            msgs += [await conv.send_message("/start")]

            msgs += [await conv.get_response()]

            msgs += [await conv.send_message(text)]

            m = await conv.get_response()

        await self._client.send_file(

            message.peer_id,

            m.media,

            caption=self.strings("mods"),

            reply_to=message.reply_to_msg_id,

        )

        for msg in msgs + [m]:

            await msg.delete()

        if message.out:

            await message.delete()

        await self.client.delete_dialog(chat)
