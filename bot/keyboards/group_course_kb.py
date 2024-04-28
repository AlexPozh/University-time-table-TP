from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choose_course() -> InlineKeyboardMarkup:
    """Ф-ция возвращает инлайн-клавиатуру для выбора курса обучения"""
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    course_kb: list[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text="1",
            callback_data="1_course"),

        InlineKeyboardButton(
            text="2",
            callback_data="2_course")
    ]

    kb_builder.row(*course_kb)

    return kb_builder.as_markup()


def choose_group(group_num: int) -> InlineKeyboardMarkup:
    """Ф-ция возвращает инлайн-клавиатуру для выбора группы обучения"""
    GROUPS: dict[str, str] = {
        1: ["23-ИСТ-1-1", "23-ИСТ-1-2", "23-ИСТ-2", "23-ИСТ-3", "23-ИСТ-4-1", "23-ИСТ-4-2"],
        2: ["22-ИСТ-1", "22-ИСТ-2", "22-ИСТ-3", "22-ИСТ-4-1", "22-ИСТ-4-2"]
    }

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    groups_kb: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text=group, callback_data=group) for group in GROUPS[group_num]
    ]
    
    kb_builder.row(*groups_kb, width=3)

    return kb_builder.as_markup()