import random

# Создаем список случайных чисел
numbers = []
for i in range(10):
    number = random.randint(-10, 10)
    numbers.append(number)

print("Исходный список чисел:", numbers)
print()

# 1. Создаем список четных чисел
even_numbers = []  # Пустой список для четных чисел
for num in numbers:
    # Проверяем, четное ли число
    if num % 2 == 0:
        even_numbers.append(num)  # Добавляем в список четных чисел

print("1. Четные числа:", even_numbers)

# 2. Создаем список нечетных чисел
odd_numbers = []  # Пустой список для нечетных чисел
for num in numbers:
    # Проверяем, нечетное ли число
    if num % 2 != 0:
        odd_numbers.append(num)  # Добавляем в список нечетных чисел

print("2. Нечетные числа:", odd_numbers)

# 3. Создаем список отрицательных чисел
negative_numbers = []  # Пустой список для отрицательных чисел
for num in numbers:
    # Проверяем, отрицательное ли число
    if num < 0:
        negative_numbers.append(num)  # Добавляем в список отрицательных чисел

print("3. Отрицательные числа:", negative_numbers)

# 4. Создаем список положительных чисел
positive_numbers = []  # Пустой список для положительных чисел
for num in numbers:
    # Проверяем, положительное ли число
    if num > 0:
        positive_numbers.append(num)  # Добавляем в список положительных чисел

print("4. Положительные числа:", positive_numbers)