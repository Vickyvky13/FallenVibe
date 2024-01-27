import random 
from pyrogram import filters 
from pyrogram.types import Message 
from unidecode import unidecode 

from AnonXMusic import app 
from AnonXMusic.misc import SUDOERS 
from AnonXMusic.utils.database import ( 
    get_active_chats, 
    get_active_video_chats, 
) 

random_photos = [ 
    "https://telegra.ph/file/06e0e6ab4c325746bd496.jpg", 
    "https://telegra.ph/file/ee4b07cdda3bdd2b6537c.jpg", 
    "https://telegra.ph/file/f3f55cad57397cd06623e.jpg", 
    # Add more URLs as needed 
] 

@app.on_message(filters.command(["vc", "a"]) & SUDOERS) 
async def active_vc_command_handler(client, message): 
    active_chats_message = await generate_active_chats_message() 
    await message.reply(active_chats_message) 

async def generate_active_chats_message(): 
    active_chats_count = str(len(await get_active_chats())) 
    active_video_chats_count = str(len(await get_active_video_chats())) 

    total_chats_count = str(int(active_chats_count) + int(active_video_chats_count)) 

    random_photo_url = random.choice(random_photos) 
    random_photo_caption = "ᴄᴜʀʀᴇɴᴛ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ & ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ʟɪꜱᴛ🤗" 

    message = ( 
        "𝗕𝗼𝘁 𝗔𝗰𝘁𝗶𝘃𝗲 𝗖𝗵𝗮𝘁𝘀 𝗜𝗻𝗳𝗼 • 🔊\n" 
        "•━━━━━━━━━━━━━━━━━━•\n" 
        f"🎧 ᴀᴜᴅɪᴏ 🎧 » {active_chats_count} Active\n" 
        "•───────•\n" 
        f"🎥 ᴠɪᴅᴇᴏ 🎥 » {active_video_chats_count} Active\n" 
        "•──────•\n" 
        f"💬 ᴛᴏᴛᴀʟ 💬 » {total_chats_count} ᴄʜᴀᴛs\n" 
        "•──────•\n" 
    ) 
    return message
