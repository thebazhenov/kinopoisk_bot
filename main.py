import asyncio

from aiogram import Dispatcher

import handlers  # noqa
from database.models import async_main
# from utils.set_bot_commands import set_default_commands
from handlers.default_handlers.start import router
from loader import bot
from utils.set_bot_commands import set_commands


async def main():

    await async_main()

    dp = Dispatcher()
    dp.include_router(router)
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')