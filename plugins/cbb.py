#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴍʏ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={OWNER_ID}'>♡ 𝚂𝙰𝙷𝙸𝙻 ♡</a>\n○ ᴍʏ ᴀᴅᴍɪɴ : @lucky1stowner \n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ  : <a href='https://t.me/itz_sahil_official'>ᴘʀɪᴠᴀᴛᴇ ᴄᴏᴅᴇ🧑‍💻</a>\n○ ᴅᴏɴᴀᴛᴇ ᴍᴇ : <a href='https://t.me/sahil_official_here/79'>ᴄʟɪᴄᴋ ᴍᴇ 😇</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏsᴇ ᴍᴇ 🥀", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
