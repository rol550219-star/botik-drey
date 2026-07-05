from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import os

# Твій токен береться зі змінних середовища, які ми налаштували
bot = Bot(token=os.getenv("8919222965:AAGWDXM37zW3mzHWuCf9B2a0taxXTEttmVM"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привіт! Я твій особистий бот. Що хочеш обговорити?")

@dp.message()
async def echo_handler(message: types.Message):
    # Тут можна додати логіку, щоб він відповідав на різні питання
    if "хто" in message.text.lower():
        await message.answer("Я — твій бот, якого ти сам створив!")
    else:
        await message.answer(f"Ти написав: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
