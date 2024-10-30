try:
    a = int(input("Введите число 1: "))
    b = int(input("Введите число 2: "))
    c = int(input("Введите число 3: "))
    x = a + b
    y = b - c
    print(x, y)
except ValueError:
    print("Ошибка: пожалуйста, введите допустимые целые числа.")
