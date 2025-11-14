"""Базовые математические операции"""

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль!")
    return a / b

def modulus(a, b):
    """Остаток от деления"""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль!")
    return a % b