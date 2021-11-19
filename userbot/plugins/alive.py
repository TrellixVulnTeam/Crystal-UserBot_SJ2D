# Thanks to @D3_krish
# Porting in REBELUSERBOT by REBEL75

import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, REBELversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "CrystalBot"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

REBEL = bot.uid

edit_time = 4
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/4356d5e1aa3ce00a2e87a.jpg"
file2 = "https://te.legra.ph/file/21a4541d14e8a70a64652.jpg"
file3 = "https://te.legra.ph/file/3082b57731ced0d858e13.jpg"
file4 = "https://te.legra.ph/file/e0e994e33fca93ec2da37.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥𝐂𝐫𝐲𝐬𝐭𝐚𝐥𝐁𝐨𝐭  𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                🔰ᗰᗩՏTᗴᖇ🔰\n      **『😈[{DEFAULTUSER}](tg://user?id={REBEL})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `𝚅𝚎𝚛𝚜𝚒𝚘𝚗:` `{REBELversion}`\n"
pm_caption += f"┣•➳➠ `𝚂𝚞𝚍𝚘:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `𝙲𝚑𝚊𝚗𝚗𝚎𝚕:` [𝙹𝙾𝙸𝙽](https://t.me/crystall_userbot)\n"
pm_caption += f"┣•➳➠ `𝙲𝚛𝚎𝚊𝚝𝚘𝚛:` [Sakshi](https://t.me/sakshii_xd)\n"
pm_caption += f"┣•➳➠ `𝙲𝚛𝚎𝚊𝚝𝚘𝚛:` [Om](https://t.me/TERA_BAAP_OM)\n"
pm_caption += f"┣•➳➠ `Do Join:` [Lovely Squad](https://t.me/Lovely_squad)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥𝐑𝐄𝐏𝐎🔥](https://github.com/SAKSHIXOM/Crystal-Bot)"

# @command(outgoing=True, pattern="^.lynx$")
@bot.on(admin_cmd(outgoing=True, pattern="crystal$"))
@bot.on(sudo_cmd(pattern="crystal$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    

    """ For .lynx command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "rebel", None, "To check am i alive with your favorite alive pic"
).add()
