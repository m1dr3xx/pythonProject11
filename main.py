import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.client import bot
from aiogram.fsm.storage.memory import MemoryStorage
from wikipedia import wikipedia

from config import config  # Config
from handlers import common, wikipedia_handlers
from keyboards.menu import main_menu_command


def register_all_routers(dp: Dispatcher):
    dp.include_routers(common.start_router, wikipedia_handlers.wiki_router)


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher(storage=MemoryStorage())  # Менеджер бота
    await bot.set_my_commands(main_menu_command)
    wikipedia.set_lang("ru")
    register_all_routers(dp)
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
