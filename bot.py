from pyrogram import Client, filters



Mikasa=Client(
  "File Store Bot",
  bot_token='5270572716:AAGYa0MpE948B9SL_Fz5aK0zxKhW-DiEGbQ',
  api_id='9969145',
  api_hash='96940e396888e9b5a2d7cf57757fc1a6 '
)

@Mikasa.on_message(filters.command("Start"))
async def start_msg(bot, msg):
  await msg.reply_text("Hi 👋🏻")
  
Mikasa.run()
  
