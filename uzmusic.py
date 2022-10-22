
# meta developer: @babycodera

from .. import loader, utils 
from asyncio import sleep 
import random 
 
__version__ = (1, 4, 0) 
 
def register(cb): 
 cb(UzMusicMod()) 
  
class UzMusicMod(loader.Module): 
 """Music List""" 
  
 strings = { "name": "UzMusic" } 

 async def aslcmd(self, message): 
  """AslWayne-Go'zlarinnan Oqmas Yoshla""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://0x0.st/oxpR.mp3", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def lolacmd(self, message): 
  """Remzi-Lola Gulim""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://0x0.st/oxp7.mp3", voice_note=True, reply_to=reply.id if reply else None) 
  return 

 async def telbacmd(self, message): 
  """AslWayne-Telba""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://0x0.st/oxph.Telba.mp", voice_note=True, reply_to=reply.id if reply else None) 
  return
