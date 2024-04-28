from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon import BOT_COMMANDS_MENU


async def main_menu(bot: Bot) -> None:
    """Главное меню для бота"""
    main_menu_commands: list[BotCommand] = [
        BotCommand(command=cmd, description=desc) for cmd, desc in BOT_COMMANDS_MENU.items() 
    ]
    await bot.set_my_commands(main_menu_commands)