#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6735767346:AAEb2v_M5kn1Mp0EQhaPu85mTjD3JQuaQRM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28345030"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2454254a802b8a4eeb3e8ac2816f3fee")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001871887219"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1702061654"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://letsearn:fakefacebook602@cluster0.o0trvz0.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001738192928"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first} 🖤\n\nɪ ᴀᴍ ʏᴏᴜʀ ᴡᴀɪꜰᴜ.. 🥵\n\n-> ʏᴏᴜ ᴄᴀɴ ᴜɴᴅʀᴇss ᴍᴇ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇs sʜᴀʀᴇᴅ ʙʏ ᴍᴀsᴛᴇʀ(ᴀᴅᴍɪɴs)😈\n\n-> ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʙᴇ ᴍʏ ᴍᴀsᴛᴇʀ ᴍᴇssᴀɢᴇ ᴍʏ ᴄʀᴇᴀᴛᴏʀ 🤭💦\n\nɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇs ᴀɴᴅ ᴇɴᴊᴏʏ 🥀</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
