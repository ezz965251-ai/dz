def calcul_sum(a, b):
    print(f"Считаем сумму чисел от {a} до {b}")
    if a < b:
        first = a
        last = b
    else:
        first = b
        last = a
    sum_result = 0
    count = 0
    print("Числа в диапазоне:")
    for num in range(first, last + 1):
        print(f"  Добавляем {num}")
        sum_result += num
        count += 1
    print(f"Всего чисел: {count}")
    print(f"Общая сумма: {sum_result}")
    return sum_result
calcul_sum(2, 4)