num1 = [3, -5, 0, 8, -2, 0, 7, -1, 4, 0]

min1 = min(num1)
max1 = max(num1)

neg = 0
pos = 0
zero = 0

for num in num1:
    if num < 0:
        neg += 1
    elif num > 0:
        pos += 1
    else:
        zero += 1

print(f"Минимальный элемент: {min1}")
print(f"Максимальный элемент: {max1}")
print(f"Количество отрицательных элементов: {neg}")
print(f"Количество положительных элементов: {pos}")
print(f"Количество нулей: {zero}")
