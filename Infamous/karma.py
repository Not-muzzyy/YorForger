# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/b8232e33e2e1d09c5687f.jpg",
    "https://telegra.ph/file/7b6bff87f37f64c155258.jpg",
    "https://telegra.ph/file/8b393e565b06884554b21.jpg",
    "https://telegra.ph/file/7a0747b2422c3fa6f2cbc.jpg",
    "https://telegra.ph/file/b563aa2159361fb120c62.jpg",
]

HEY_IMG = "https://telegra.ph/file/b8232e33e2e1d09c5687f.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "*✨ ɪ ᴀᴍ ʏᴏʀ ғᴏʀɢᴇʀ, 
ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇᴅ sᴘʏ x ғᴀᴍɪʟʏ  ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ 𝗔𝗗𝗗 𝗠𝗘 ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="𝗔𝗕𝗢𝗨𝗧 𝗠𝗘", callback_data="Miko_"),
        InlineKeyboardButton(text="𝗔𝗜", callback_data="ai_handler"),
    ],
    [
        InlineKeyboardButton(text="⚡ 𝗠𝗬 𝗠𝗔𝗦𝗧𝗘𝗥 ⚡", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ 𝗔𝗗𝗗 𝗠𝗘 ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="⚡ 𝗠𝗬 𝗠𝗔𝗦𝗧𝗘𝗥 ⚡", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/vizxer_official"),
        ib(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/Rulers_Authority"),
    ],
    [
        ib(
            text="⇦ 𝗔𝗗𝗗 𝗠𝗘 ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *𝗬𝗢𝗥 𝗙𝗢𝗥𝗚𝗘𝗥* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
