def find_max_of_four(a, b, c, d):
    max_number = a
    if b > max_number:
        max_number = b
    if c > max_number:
        max_number = c
    if d > max_number:
        max_number = d
    return max_number
result = find_max_of_four(3, 7, 2, 9)
print(f"Максимальное число: {result}")