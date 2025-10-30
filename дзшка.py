number = input("Введите арифметическое выражение (например, 23+12): ")
if '+' in number:
    num1, num2 = number.split('+')
    result = float(num1) + float(num2)
elif '-' in number:
    num1, num2 = number.split('-')
    result = float(num1) - float(num2)
elif '*' in number:
    num1, num2 = number.split('*')
    result = float(num1) * float(num2)
elif '/' in number:
    num1, num2 = number.split('/')
    if float(num2) == 0:
        print("Ошибка: деление на ноль!")
        exit()
    result = float(num1) / float(num2)
else:
    print("Ошибка: неверный формат выражения")
    exit()

print(f"Результат: {result}")