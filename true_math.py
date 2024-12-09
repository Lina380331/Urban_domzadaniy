def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Бесконечность.")

# Пример использования функции
a = 99
b = 0

divide(a, b)