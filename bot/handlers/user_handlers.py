from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from lexicon.lexicon import LEXICON_RU

from keyboards.group_course_kb import choose_group, choose_course


router: Router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    """Ф-ция обработчик, отвечающая за обработку команды /start"""
    await message.answer(
        text=LEXICON_RU[message.text]
    )


@router.message(Command("help"))
async def help_command(message: Message):
    """Ф-ция обработчик, отвечающая за обработку команды /help"""
    await message.answer(
        text=LEXICON_RU[message.text]
    )


@router.message(Command("choose_group"))
async def choose_gp_command(message: Message):
    """Ф-ция обработчик, отвечающая за обработку команды /choose_group"""
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=choose_course()
    )