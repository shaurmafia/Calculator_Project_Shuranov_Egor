"""Операции с валютой"""

exchange_rate = None

def set_exchange_rate(rate):
    """Установка курса валюты"""
    global exchange_rate
    exchange_rate = rate
    return f"Курс установлен: 1 единица = {rate} рублей"

def set_exchange_rate_interactive():
    """Интерактивная установка курса валюты"""
    global exchange_rate
    try:
        rate = float(input("Введите актуальный курс валюты (например, 95.5 для доллара): "))
        exchange_rate = rate
        return f"Курс установлен: 1 единица = {rate} рублей"
    except ValueError:
        return "Ошибка: Введите корректное число!"

def convert_currency(amount):
    """Конвертация валюты"""
    global exchange_rate
    if exchange_rate is None:
        raise ValueError("Сначала установите курс валюты!")
    return amount * exchange_rate

def get_exchange_rate():
    """Получить текущий курс"""
    return exchange_rate
