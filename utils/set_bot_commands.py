from loader import bot
from aiogram import Bot
from config_data.config import commands


async def set_commands(bot: Bot):
    await bot.set_my_commands(commands)