import os
from aiogram.types import BotCommand
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
SQL_ALCHEMY_URL = os.getenv("SQL_ALCHEMY_URL")
commands = [
        BotCommand(command="/start", description="Начать работу"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/info", description="Информация"),
        BotCommand(command="/catalog", description="Перейти в каталог"),
    ]
