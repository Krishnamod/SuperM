import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fd880593afcb71a2c02cd.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ᴀʟɪsʜᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴄᴀᴅᴇɴ ᴏᴘ](https://t.me/Caden_OP)
┣★ ᴜᴘᴅᴀᴛᴇs : [ᴄᴀᴅᴇɴ sᴇʀᴠᴇʀ](https://t.me/VAMPIRE_EMPIRE_OFFICIAL)
┣★ sᴜᴘᴘᴏʀᴛ : [ʜᴀᴄᴋɪɴɢ ᴄʜᴀɴɴᴇʟ](https://t.me/CADEN_VampireYT)
┣★ ᴏᴡɴᴇʀ › : [Cᴀɴᴅʏ ǫᴜᴇᴇɴ](https://t.me/CADEN_VampireYT)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/Caden_OP) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ʜᴇʀᴇ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ❱ ➕", url=f"https://t.me/VAMPIRE_EMPIRE_OFFICIAL")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "Caden"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/33a6f809c3ce77cdf51be.jpg",

        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
ᴄᴀᴅᴇɴ ɪs ᴍʏ ᴏᴡɴᴇʀ😎 ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ɪssᴜᴇ🙁 ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ❣️🌹] [ᴄᴀᴅᴇɴ](https://t.me/Caden_OP)
━━━━━━━━━━━━━━━━━━━━━━━━**""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "ᴄᴀᴅᴇɴ's ᴡɪғᴇ❣️", url=f"https://t.me/Caden_XD")

                ]

            ]

        ),

    )

@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/758536a9512a84422bf2a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://t.me/CADEN_VampireYT")
                ]
            ]
        ),
    )
