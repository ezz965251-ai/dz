def find_odd_numbers(a, b):
    print(f"Ищем нечетные числа от {a} до {b}")
    if a < b:
        first = a
        last = b
    else:
        first = b
        last = a
    count = 0
    for num in range(first, last + 1):
        if num % 2 == 1:
            print(f"Нашли нечетное число: {num}")
            count += 1

    print(f"Всего найдено нечетных чисел: {count}")
find_odd_numbers(1, 10)