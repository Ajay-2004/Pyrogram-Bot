from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


Mikasa=Client(
  "File Store Bot",
  bot_token='5270572716:AAGYa0MpE948B9SL_Fz5aK0zxKhW-DiEGbQ',
  api_id='14562867',
  api_hash='c54613404f9bcdbd0c90171e346de396'
)

@Mikasa.on_message(filters.command("Start"))
async def start_msg(bot: Mikasa, msg: Message):
  await msg.reply_text(
    text="I'm Mikasa㊗️, an file store bot with greater abilities",
    reply_markup=InlineKeyboardMarkup( [[
      InlineKeyboardButton("Çhåññêl", url="https://t.me/+7xdSoB4FSkphZTE1"),
      InlineKeyboardButton("Grðµþ" , url="https://t.me/doflix_studios")
      
      
      
    
    ]]
    )
  )
    
      
    
    
    
    
    
    

@Mikasa.on_message(filters.command("Help"))
async def help_msg(bot: Mikasa, msg: Message):
  await msg.reply_text("<b>Help</b>🏻")
  
Mikasa.run()
  
