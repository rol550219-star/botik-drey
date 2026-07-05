from aiogram import Bot, Dispatcher, types, F
import asyncio

# Встав сюда токен своего нового бота
TOKEN = "8919222965:AAGWDXM37zW3mzHWuCf9B2a0taxXTEttmVM"

dp = Dispatcher()

# Приветствие
@dp.message(F.text == "/start")
async def start(message: types.Message):
    await message.answer("Привет! Я твой личный бот. О чем хочешь пообщаться?")

# Логика ответов
@dp.message()
async def chat(message: types.Message):
    user_text = message.text.lower()
    
    if "привет" in user_text:
        await message.answer("Привет! Как дела?")
    elif "как дела" in user_text:
        await message.answer("У меня всё отлично! А у тебя?")
    elif "кто ты" in user_text:
        await message.answer("Я твой личный чат-бот, которого ты сам создал!")
    elif "что делаешь" in user_text:
        await message.answer("Общаюсь с тобой, конечно!")
    else:
        # Если бот не знает, что ответить, он ответит это:
        await message.answer("Интересно... расскажи подробнее?")

async def main():
    bot = Bot(token=TOKEN)
    print("Бот запущен и готов к общению!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
                             
