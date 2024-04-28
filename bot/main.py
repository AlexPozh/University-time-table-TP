# import sys

# print(sys.path)



import asyncio

from aiogram import Dispatcher, Bot

from config_bot import get_bot_config

from handlers import user_handlers, callback_queries

from keyboards.main_menu import main_menu



async def main() -> None:
    """Точка входа программы бота"""

    bot = Bot(get_bot_config().bot_token, 
              parse_mode="HTML")

    dp = Dispatcher()

    # главное меню бота
    await main_menu(bot)

    # подключение дочерних роутеров к родительскому
    dp.include_router(user_handlers.router)
    dp.include_router(callback_queries.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())