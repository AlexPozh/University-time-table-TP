from openpyxl import load_workbook

from additional_funcs import get_cell_value, check_cell

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
GROUPS_TIMETABLE: dict[str, dict[str, list[str]]] = {}


def formatted_output(day, time_and_num_lesson, lesson_name) -> tuple[str] | None:
    """Ф-ция форматирования расписания."""
    if day is None or time_and_num_lesson is None or lesson_name is None:    # если None хотя бы одна из перменных, то возвращаем None
        return 
    
    return day.strip(), time_and_num_lesson.strip(), " ".join(lesson_name.strip().split())

book = load_workbook("/home/alexander/Рабочий стол/Uni_time_table_IRIT/Bot_uni_time_table/files_timetable/1_kurs_IRIT.xlsx")    # абсолютный путь до файла

ist_table = book["ист"]    # извлекаем отдельную таблицу для групп ИСТ


IST_GROUPS: dict[str, tuple[str]] = {   # словарь содержит координаты ячеек групп и их расписания
    "C10": ("A", "B", "C"),
    "E10": ("A", "B", "E"),
    "G10": ("A", "B", "G"),
    "I10": ("A", "B", "I"),
    "K10": ("A", "B", "K"),
    "M10": ("A", "B", "M"),
}

def parse_groups(table) -> None:
    """Ф-ция для парсинга групп ИСТ.
    table: таблица групп / worksheet"""
    for group_cell, value_cells in IST_GROUPS.items(): 

        group =  get_cell_value(table[group_cell])

        GROUPS_TIMETABLE[group] = {}    # создаем ключ - группу, а значение - пустой словарь

        # извлечение данных из ячеек
        for n in range(11, 89, 2):
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

parse_groups(ist_table)    

pprint(GROUPS_TIMETABLE)    























