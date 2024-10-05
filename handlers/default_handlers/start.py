from handlers.imports import CommandStart, Message
from handlers.routers import router


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, меня зовут Роман! Я ученик Skillbox. Добро пожаловать, в тестовый бот')
