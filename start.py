from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboard import contact_keyboard

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum!\n\nTelefon raqamingizni yuboring.",
        reply_markup=contact_keyboard
    )