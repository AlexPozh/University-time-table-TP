from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon import LEXICON_DAYS

def weekdays() -> InlineKeyboardMarkup:
    """Ф-ция возвращает инлайн-клавиатуру для выбора дня"""
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    kb_builder.row(
        *[
            InlineKeyboardButton(
            text=short_title,
            callback_data=long_title) for long_title, short_title in LEXICON_DAYS.items()
            ]
    )

    return kb_builder.as_markup()