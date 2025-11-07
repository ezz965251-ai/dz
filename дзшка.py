import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10, 10))

print("Список чисел:", numbers)
print()

sum_negative = 0
for num in numbers:
    if num < 0:
        sum_negative += num
print("1. Сумма отрицательных чисел:", sum_negative)

sum_even = 0
for num in numbers:
    if num % 2 == 0:  # Если число делится на 2 без остатка
        sum_even += num
print("2. Сумма четных чисел:", sum_even)

sum_odd = 0
for num in numbers:
    if num % 2 != 0:  # Если число не делится на 2 без остатка
        sum_odd += num
print("3. Сумма нечетных чисел:", sum_odd)

product_index_3 = 1
for i in range(len(numbers)):
    if i % 3 == 0 and i != 0:  # Индексы 3, 6, 9 и т.д. (кроме 0)
        product_index_3 *= numbers[i]
print("4. Произведение элементов с индексами кратными 3:", product_index_3)

min_num = numbers[0]
max_num = numbers[0]
min_index = 0
max_index = 0

for i in range(len(numbers)):
    if numbers[i] < min_num:
        min_num = numbers[i]
        min_index = i
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_index = i

print("   Минимальный элемент:", min_num, "на позиции", min_index)
print("   Максимальный элемент:", max_num, "на позиции", max_index)

product_between = 1
start = min(min_index, max_index) + 1
end = max(min_index, max_index)

# Умножаем все числа между min и max
for i in range(start, end):
    product_between *= numbers[i]

print("5. Произведение между min и max:", product_between)

first_positive_index = -1
for i in range(len(numbers)):
    if numbers[i] > 0:
        first_positive_index = i
        break

last_positive_index = -1
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > 0:
        last_positive_index = i
        break

print("   Первый положительный на позиции:", first_positive_index)
print("   Последний положительный на позиции:", last_positive_index)

sum_between_positive = 0
if first_positive_index != -1 and last_positive_index != -1:
    start_pos = min(first_positive_index, last_positive_index) + 1
    end_pos = max(first_positive_index, last_positive_index)

    for i in range(start_pos, end_pos):
        sum_between_positive += numbers[i]

print("6. Сумма между первым и последним положительными:", sum_between_positive)