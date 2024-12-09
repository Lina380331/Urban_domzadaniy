
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль.")

# Пример использования функции
a = 78
b = 0

divide(a, b)