def find_min_index(numbers):
    if len(numbers) == 0:
        return -1

    min_value = numbers[0]
    min_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < min_value:
            min_value = numbers[i]
            min_index = i

    return min_index

list1 = [5, 2, 8, 1, 9, 3]
result1 = find_min_index(list1)
print(f"Список: {list1}")
print(f"Индекс минимального элемента: {result1}")
print(f"Минимальный элемент: {list1[result1]}")
print()

list2 = [10, -5, 7, -8, 0, 15]
result2 = find_min_index(list2)
print(f"Список: {list2}")
print(f"Индекс минимального элемента: {result2}")
print(f"Минимальный элемент: {list2[result2]}")
print()

list3 = [-3, -1, -7, -2, -5]
result3 = find_min_index(list3)
print(f"Список: {list3}")
print(f"Индекс минимального элемента: {result3}")
print(f"Минимальный элемент: {list3[result3]}")
print()

list4 = []
result4 = find_min_index(list4)
print(f"Пустой список: {list4}")
print(f"Результат для пустого списка: {result4}")