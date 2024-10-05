from handlers.routers import router
from handlers.imports import Command, Message


@router.message(Command('search'))
async def search_films(message: Message):
    """  Функция для поиска фильмов по определенному названию"""
    await message.answer('Команда для поиска фильмов')