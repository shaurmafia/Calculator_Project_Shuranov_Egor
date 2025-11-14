"""Продвинутые математические операции"""
import math

def power(a, b):
    """Возведение в степень"""
    return a ** b

def square_root(a):
    """Квадратный корень"""
    if a < 0:
        raise ValueError("Ошибка: Корень из отрицательного числа!")
    return math.sqrt(a)

def cube_root(a):
    """Кубический корень"""
    return a ** (1/3)

def compare_numbers(a, b):
    """Сравнение двух чисел"""
    if a > b:
        return f"{a} > {b}"
    elif a < b:
        return f"{a} < {b}"
    else:
        return f"{a} = {b}"

def percentage(a, b):
    """Вычисление процента от числа"""
    return (a * b) / 100