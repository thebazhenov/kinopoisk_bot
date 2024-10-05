from handlers.routers import router
from handlers.imports import F, Message


@router.message(F.text)
async def text(message: Message):
    await message.answer('Вы ввели текст. Неизвестная команда!')
