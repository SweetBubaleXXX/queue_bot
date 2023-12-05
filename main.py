from datetime import datetime
from os import getenv
from random import seed, shuffle

from pyrogram import Client, filters

api_id = getenv("API_ID")
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("who") & filters.group)
async def order_queue(client, message):
    members = sorted(
        [member async for member in app.get_chat_members(message.chat.id)],
        key=lambda member: member.user.id,
    )
    timestamp = int(datetime.now().strftime("%Y%m%d"))
    seed(timestamp)
    shuffle(members)
    response = "\n".join(
        (f"**{n+1}**. {member.user.mention}" for n, member in enumerate(members))
    )
    await message.reply(response)


if __name__ == "__main__":
    app.run()
