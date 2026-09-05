import os import asyncio
from aiogram import Bot, Dispatcher from aiogram.filters import CommandStart from aiogram.types import Message from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN: raise ValueError("BOT_TOKEN topilmadi!")
bot = Bot(token=BOT_TOKEN) dp = Dispatcher()
@dp.message(CommandStart()) async def start_handler(message: Message): await message.answer( "👋 Assalomu alaykum!\n\n" "🛍 UNIT 09 ga xush kelibsiz!\n\n" "Bu yerda kiyimlarni ko‘rishingiz va buyurtma berishingiz mumkin." )
async def main(): print("UNIT 09 bot ishga tushdi!") await dp.start_polling(bot)
if name == "main": asyncio.run(main())
