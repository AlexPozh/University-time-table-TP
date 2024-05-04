from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


router: Router = Router()


@router.message(F.content_type.in_(['audio', "sticker", "photo", "voice", "video", "animation"]))
async def echo_message(message: Message):
    await message.reply(
        text="Извините, но я понимаю только команды из списка menu😞😞"
    )
    print(f"Апдейт от пользователя c id{message.from_user.id} попал в ф-цию echo_message()")