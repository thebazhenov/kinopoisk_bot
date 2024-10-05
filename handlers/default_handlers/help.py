from aiogram import Router
from handlers.routers import router
from handlers.imports import Message, CommandStart, Command
from loader import bot


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('КОМАНДЫ ДЛЯ ПОМОЩИ ВАМ НЕГРЫ:')

