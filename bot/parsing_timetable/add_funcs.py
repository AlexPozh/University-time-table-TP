from openpyxl.cell import Cell, MergedCell

def find_parent_merged_cell(cell: Cell | MergedCell) -> None | str:
    """Ф-ция находит родителя для переданной клетки"""
    sheet = cell.parent                            # получаем лист / таблицу для данной ячейки
    child_coord = cell.coordinate                  # получаем координату переданной ячейки
    for merged in sheet.merged_cells.ranges:       # итерируемся по всем объединенным ячейкам
        if child_coord in merged:                  # проверяем на вхождение нашей ячейки в объединенный участок
            return merged.start_cell.coordinate    # возвращаем координаты первой ячейки, потому что только первая ячейка хранит значение для всех объединенных ячеек
    return None


def get_cell_value(cell: Cell | MergedCell) -> str:
    """Ф-ция возвращает значение для ячейки с проверкой на объединенность."""
    if isinstance(cell, Cell):                      # если ячейка ялвяется не объединенной, то возвращаем ее значение
        return cell.value
    if isinstance(cell, MergedCell):                # если ячейка ялвяется объединенной, то возвращаем значение первой клетки из объединенного диапазона
        first_cell_coord = find_parent_merged_cell(cell)    # координаты первой клетки из диапазона
        return cell.parent[first_cell_coord].value
    

def check_cell(cell: Cell) -> str:
    """Ф-ция проверяет значение ячейки на None"""
    return cell.value if cell.value is not None else ""