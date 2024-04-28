# import sys
# sys.path.append('/home/alexander/Рабочий стол/Uni_time_table_IRIT/Bot_uni_time_table/bot')



from openpyxl import load_workbook

from .add_funcs import get_cell_value, check_cell

from pprint import pprint

# шаблон словаря GROUPS_TIMETABLE
"""
{
    группа_1: {
        пн: [1-ая пара, 2-ая пара, ...],
        вт: [1-ая пара, 2-ая пара, ...],
        ср: [1-ая пара, 2-ая пара, ...],
        ...
    },
    группа_2: {
        пн: [1-ая пара, 2-ая пара, ...],
        ...
    },
    ...
}
"""


def formatted_output(day, time_and_num_lesson, lesson_name) -> tuple[str] | None:
    """Ф-ция форматирования расписания."""
    if day is None or time_and_num_lesson is None or lesson_name is None:    # если None хотя бы одна из перменных, то возвращаем None
        return 
    return day.strip(),  "<b><u>" + time_and_num_lesson.strip() + "</u></b>", " ".join(lesson_name.strip().split())


book = load_workbook("/home/alexander/Рабочий стол/Uni_time_table_IRIT/Bot_uni_time_table/bot/parsing_timetable/files_timetable/2_kurs_IRIT.xlsx")    # абсолютный путь до файла

ist_table = book["ист"]    # извлекаем отдельную таблицу для групп ИСТ


IST_GROUPS: dict[str, tuple[str]] = {   # словарь содержит координаты ячеек групп и их расписания
    "F11": ("D", "E", "F"),
    "H11": ("D", "E", "H"),
    "J11": ("D", "E", "J"),
    "L11": ("D", "E", "L"),
    "N11": ("D", "E", "N")
}


def parse_groups() -> None:
    """Ф-ция для парсинга групп ИСТ."""
    GROUPS_TIMETABLE: dict[str, dict[str, list[str]]] = {}

    for group_cell, value_cells in IST_GROUPS.items(): 

        group =  get_cell_value(ist_table[group_cell])

        GROUPS_TIMETABLE[group] = {}    # создаем ключ - группу, а значение - пустой словарь

        # извлечение данных из ячеек
        for n in range(12, 83, 2):
            day = get_cell_value(ist_table[value_cells[0] + str(n)])
            num_lesson_and_time = f"{get_cell_value(ist_table[value_cells[1] + str(n)])} {get_cell_value(ist_table[value_cells[1] + str(n + 1)])}"
            lesson_name = f"{get_cell_value(ist_table[value_cells[2] + str(n)])} {check_cell(ist_table[value_cells[2] + str(n+1)])}"

            schedule = formatted_output(day, num_lesson_and_time, lesson_name)

            # добавление в словарь
            if schedule is None or schedule[2] == "None":
                continue
            else:
                if schedule[0] in GROUPS_TIMETABLE[group].keys():
                    GROUPS_TIMETABLE[group][schedule[0]].append(schedule[1] + " " + schedule[2]) 
                else:
                    GROUPS_TIMETABLE[group][schedule[0]] = [schedule[1] + " " + schedule[2]]
    return GROUPS_TIMETABLE

# pprint(parse_groups())  

# ПРОВЕРКА РАСПИСАНИЯ
# for key, value in GROUPS_TIMETABLE['22 ИСТ-4-2 (21)'].items():
#     print(key)
#     for day in value:
#         print(day)
#     print("-"*15)

 
