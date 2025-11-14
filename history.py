"""Управление историей вычислений"""

calculation_history = []

def record_history(calculation):
    """Запись в историю вычислений"""
    calculation_history.append(calculation)
    # Ограничиваем историю последними 10 операциями
    if len(calculation_history) > 10:
        calculation_history.pop(0)

def show_history():
    """Показать историю вычислений"""
    return calculation_history.copy()

def clear_history():
    """Очистить историю"""
    calculation_history.clear()

def get_history_count():
    """Получить количество записей в истории"""
    return len(calculation_history)