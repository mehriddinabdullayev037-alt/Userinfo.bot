from aiogram import Router
from aiogram.types import Message

from send_group import send_user

router = Router()

@router.message(lambda message: message.contact)
async def contact(message: Message):

    await send_user(message.bot, message.from_user)

    await message.answer(
        "✅ Ma'lumotlaringiz qabul qilindi."
    )