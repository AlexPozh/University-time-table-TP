from environs import Env

from dataclasses import dataclass

env: Env = Env()

env.read_env()          # считываем переменное окружение

@dataclass              # датакласс конфига бота
class BotConfig:
    bot_token : str


def get_bot_config() -> BotConfig:
    """Ф-ция возвращает ссылку на класс конфига бота."""
    return BotConfig(bot_token=env("BOT_TOKEN"))