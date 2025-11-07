def sort_numbers_string(input_string):
    parts = input_string.split()

    numbers = []

    for part in parts:
        number = int(part)
        numbers.append(number)
    numbers.sort()

    result_string = ""
    for i in range(len(numbers)):
        result_string += str(numbers[i])
        if i < len(numbers) - 1:
            result_string += " "

    return result_string

input1 = "5 2 8 1 9 3"
result1 = sort_numbers_string(input1)
print(f"Входная строка: '{input1}'")
print(f"Результат: '{result1}'")
print()

input2 = "10 -5 7 -8 0 15"
result2 = sort_numbers_string(input2)
print(f"Входная строка: '{input2}'")
print(f"Результат: '{result2}'")
print()

input3 = "100 50 25 75"
result3 = sort_numbers_string(input3)
print(f"Входная строка: '{input3}'")
print(f"Результат: '{result3}'")
print()

input4 = "-3 -1 -7 -2 -5"
result4 = sort_numbers_string(input4)
print(f"Входная строка: '{input4}'")
print(f"Результат: '{result4}'")