from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def back_button() -> InlineKeyboardMarkup:
    """Ф-ция возвращает инлайн-клавиатуру для возврата назад"""
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    back_kb: list[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text="<<",
            callback_data="back_weekdays")
    ]

    kb_builder.row(*back_kb)

    return kb_builder.as_markup()

