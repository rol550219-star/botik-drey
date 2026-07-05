import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен береться з налаштувань Render (Environment Variables)
bot = Bot(token=os.getenv("8919222965:AAGWDXM37zW3mzHWuCf9B2a0taxXTEttmVM"))
dp = Dispatcher()

# Обробник команди /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привіт! Я твій особистий бот. Про що хочеш поспілкуватися?")

# Обробник усіх інших повідомлень
@dp.message()
async def echo_handler(message: types.Message):
    text = message.text.lower()
    
    if "ти хто" in text or "ты кто" in text:
        await message.answer("Я — твій особистий бот, якого ти створив!")
    elif "як справи" in text or "как дела" in text:
        await message.answer("У мене все відмінно, працюю без вихідних! А у тебе?")
    elif "нормально" in text:
        await message.answer("Радий чути! Може, хочеш щось обговорити?")
    else:
        await message.answer("Це цікаво! Розкажи про це докладніше?")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
