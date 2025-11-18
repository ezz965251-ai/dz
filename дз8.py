def check_luck_num(num):
    print(f" Проверяем число {num}:")
    num_string = str(num)
    print(f"Цифры числа: {list(num_string)}")
    first_three = num_string[0:3]
    last_three = num_string[3:6]
    print(f"Первые три цифры: {first_three}")
    print(f"Последние три цифры: {last_three}")
    sum1 = 0
    print("Считаем сумму первых трех цифр:")
    for digit in first_three:
        sum1 += int(digit)
        print(f"  +{digit} = {sum1}")
    sum2 = 0
    print("Считаем сумму последних трех цифр:")
    for digit in last_three:
        sum2 += int(digit)
        print(f"  +{digit} = {sum2}")
    print(f"Сумма первых трех: {sum1}")
    print(f"Сумма последних трех: {sum2}")
    if sum1 == sum2:
        print("Суммы равны - число СЧАСТЛИВОЕ!")
        return True
    else:
        print("Суммы не равны - число НЕ счастливое")
        return False
check_luck_num(123420)
check_luck_num(723422)