"""Основная логика приложения"""
from basic_operations import add, subtract, multiply, divide, modulus
from advanced_operations import power, square_root, cube_root, compare_numbers, percentage
from currency_operations import set_exchange_rate_interactive, convert_currency, get_exchange_rate
from history import record_history, show_history
from menu import display_menu, display_welcome

def get_number(prompt):
    """Безопасный ввод числа"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число!")

def main():
    """Основная функция программы"""
    display_welcome()
    
    while True:
        display_menu()
        
        try:
            choice = input("Введите номер операции: ").strip()
            
            if choice == "1":  # Сложение
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                result = add(a, b)
                record_history(f"{a} + {b} = {result}")
                print(f"Результат: {a} + {b} = {result}")
                
            elif choice == "2":  # Вычитание
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                result = subtract(a, b)
                record_history(f"{a} - {b} = {result}")
                print(f"Результат: {a} - {b} = {result}")
                
            elif choice == "3":  # Умножение
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                result = multiply(a, b)
                record_history(f"{a} * {b} = {result}")
                print(f"Результат: {a} * {b} = {result}")
                
            elif choice == "4":  # Деление
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                try:
                    result = divide(a, b)
                    record_history(f"{a} / {b} = {result}")
                    print(f"Результат: {a} / {b} = {result}")
                except ValueError as e:
                    print(e)
                    
            elif choice == "5":  # Возведение в степень
                a = get_number("Введите основание: ")
                b = get_number("Введите степень: ")
                result = power(a, b)
                record_history(f"{a} ^ {b} = {result}")
                print(f"Результат: {a} ^ {b} = {result}")
                
            elif choice == "6":  # Квадратный корень
                a = get_number("Введите число: ")
                try:
                    result = square_root(a)
                    record_history(f"√{a} = {result}")
                    print(f"Результат: √{a} = {result}")
                except ValueError as e:
                    print(e)
                    
            elif choice == "7":  # Кубический корень
                a = get_number("Введите число: ")
                result = cube_root(a)
                record_history(f"∛{a} = {result}")
                print(f"Результат: ∛{a} = {result}")
                
            elif choice == "8":  # Остаток от деления
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                try:
                    result = modulus(a, b)
                    record_history(f"{a} % {b} = {result}")
                    print(f"Результат: {a} % {b} = {result}")
                except ValueError as e:
                    print(e)
                    
            elif choice == "9":  # Сравнение чисел
                a = get_number("Введите первое число: ")
                b = get_number("Введите второе число: ")
                result = compare_numbers(a, b)
                record_history(f"Сравнение: {result}")
                print(f"Результат: {result}")
                
            elif choice == "10":  # Проценты
                a = get_number("Введите число: ")
                b = get_number("Введите процент: ")
                result = percentage(a, b)
                record_history(f"{b}% от {a} = {result}")
                print(f"Результат: {b}% от {a} = {result}")
                
            elif choice == "11":  # Установка курса валюты
                message = set_exchange_rate_interactive()
                print(message)
                
            elif choice == "12":  # Конвертер валют
                if get_exchange_rate() is None:
                    print("Сначала установите курс валюты!")
                    message = set_exchange_rate_interactive()
                    print(message)
                    if get_exchange_rate() is None:
                        continue
                
                amount = get_number("Введите количество валюты: ")
                try:
                    result = convert_currency(amount)
                    record_history(f"Конвертация: {amount} * {get_exchange_rate()} = {result} рублей")
                    print(f"Результат: {amount} единиц = {result} рублей")
                except ValueError as e:
                    print(e)
                        
            elif choice == "13":  # История вычислений
                history = show_history()
                if not history:
                    print("История вычислений пуста")
                else:
                    print("\nИстория вычислений:")
                    for i, calc in enumerate(history, 1):
                        print(f"{i}. {calc}")
                        
            elif choice == "14":  # Выход
                print("Спасибо за использование Calculator! До свидания!")
                break
                
            else:
                print("Ошибка: Выберите номер от 1 до 14!")
                
        except KeyboardInterrupt:
            print("\nПрограмма прервана. До свидания!")
            break
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()