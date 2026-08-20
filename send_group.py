from config import GROUP_ID

async def send_user(bot, user):
    text = f"""
📥 Yangi foydalanuvchi

🆔 ID: {user.id}
👤 Ism: {user.first_name}
👤 Familiya: {user.last_name}
📛 Username: @{user.username}
⭐ Premium: {user.is_premium}
"""

    await bot.send_message(GROUP_ID, text)