import sys
sys.path.append('/home/alexander/Рабочий стол/Uni_time_table_IRIT/Bot_uni_time_table/bot')
# print(sys.path)

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, default_state, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import StateFilter

from keyboards.group_course_kb import choose_group
from keyboards.weekdays import weekdays
from keyboards.functional_btns import back_button



from parsing_timetable import parse_1_course_IRIT, parse_2_course


storage: MemoryStorage = MemoryStorage()    # хранилище для состояний и их данных


class StudentGroup(StatesGroup):
    student_group = State()


router: Router = Router()


@router.callback_query(F.data.in_(["1_course", "2_course"]))
async def show_groups(callback: CallbackQuery, state: FSMContext):
    """Ф-ция обрабатывает коллбэк на выбор курса и показывает список групп на этом курсе."""
    await callback.message.edit_text(
        text="Выберите группу:",
        reply_markup=choose_group(int(callback.data[0]))
    )
    await state.update_data(course=int(callback.data[0]))

    await state.set_state(StudentGroup.student_group)
    


@router.callback_query(F.data.in_(["23-ИСТ-1-1", "23-ИСТ-1-2", "23-ИСТ-2", "23-ИСТ-3", "23-ИСТ-4-1", "23-ИСТ-4-2", "22-ИСТ-1", "22-ИСТ-2", "22-ИСТ-3", "22-ИСТ-4-1", "22-ИСТ-4-2"]), StateFilter(StudentGroup.student_group))
async def show_weekdays(callback: CallbackQuery,  state: FSMContext):
    """Ф-ция показывает дни недели для групп"""
    await state.update_data(group=callback.data)

    print("Im in show_weekdays()")
    data = await state.get_data()
    print(data)

    await callback.message.edit_text(
        text=f"Расписание для группы {callback.data}:",
        reply_markup=weekdays()
    )


@router.callback_query(F.data.in_(["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]))
async def show_schedule_for_group(callback: CallbackQuery,  state: FSMContext):
    """Ф-ция показывает расписание на выбранный день для выбранной группы"""
    
    print("Im in show_schedule_for_group()")
    data = await state.get_data()
    print(data)

    group = data["group"]
    course = data["course"]

    if course == 1:
        timetable_1_course = parse_1_course_IRIT.parse_groups()
        await callback.message.edit_text(
            text="\n\n".join(timetable_1_course[group].get(callback.data, "Нет пар")),
            reply_markup=back_button()
        )

    elif course == 2:
        timetable_2_course = parse_2_course.parse_groups()
        await callback.message.edit_text(
            text="\n\n".join(timetable_2_course[group].get(callback.data, "Нет пар")),
            reply_markup=back_button()
        )


@router.callback_query(F.data == "back_weekdays")
async def back_weekds(callback: CallbackQuery, state: FSMContext):
    """Ф-ция возврата назад к группе"""
    data = await state.get_data()

    group = data["group"]

    await callback.message.edit_text(
        text=f"Расписание для группы {group}:",
        reply_markup=weekdays()
    )