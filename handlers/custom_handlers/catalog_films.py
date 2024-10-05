from handlers.imports import Command, Message
from handlers.routers import router


@router.message(Command('catalog'))
async def catalog(message: Message):
    """ Функция для выдачи пользователю каталога с фильмами"""
    await message.answer('Каталог с фильмами:')
