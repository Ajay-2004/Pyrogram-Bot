from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random

Mikasa=Client(
  "File Store Bot",
  bot_token='5270572716:AAGYa0MpE948B9SL_Fz5aK0zxKhW-DiEGbQ',
  api_id='14562867',
  api_hash='c54613404f9bcdbd0c90171e346de396'
)

START_PIC = [
  "https://telegra.ph/file/570f62a57bbd6c7263df9.jpg",
  "https://telegra.ph/file/e3327443ac3ab5e6c4daa.jpg",
  "https://telegra.ph/file/feae2a0fe4fc4388ca385.jpg"
]  


@Mikasa.on_message(filters.command("Start"))
async def start_msg(bot: Mikasa, msg: Message):
  await msg.reply_photo(
    photo=random.choice(START_PIC),
    caption="I'm Mikasa ㊗️, an file store bot with greater abilities",
    reply_markup=InlineKeyboardMarkup( [[
      InlineKeyboardButton("CHANNEL", url="https://t.me/+7xdSoB4FSkphZTE1"),
      InlineKeyboardButton("GROUP", url="https://t.me/doflix_studios")
    ],[
      InlineKeyboardButton("HELP", url="https://t.me/doflix_support")
      
      
    
    ]]
    )
  )
    
      
    
    
    
    
    
    

@Mikasa.on_message(filters.command("Help"))
async def help_msg(bot: Mikasa, msg: Message):
  await msg.reply_text("<b>Help</b>🏻")
  
Mikasa.run()
  
