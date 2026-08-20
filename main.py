import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN

from start import router as start_router
from contact import router as contact_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(contact_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Hammasi chotki...")
    asyncio.run(main())