from telegram import Bot

async def get_chat_id(bot_token):
    bot = Bot(token=bot_token)
    updates = await bot.get_updates()
    chat_id = updates[-1].message.chat_id
    return chat_id

bot_token = '6076516683:AAGxiCyRhN9Vk4n2KEy0x621ZjMMzGEu8Cs'  # Replace with your actual bot token

import asyncio
loop = asyncio.get_event_loop()
chat_id = loop.run_until_complete(get_chat_id(bot_token))
print(f"Chat ID: {chat_id}")
