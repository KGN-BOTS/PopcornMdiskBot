from pyrogram import Client
from config import *

API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN
ADMIN = ADMINS

bot = Client('droplink search bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=dict(root="plugins"),
             workers=50,
    sleep_threshold=10)

print("Bot Started")

# Running the bot.
bot.run()

