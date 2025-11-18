def check_prime(n):
    print(f"Проверяем число {n}:")
    if n < 2:
        print(f"Число {n} меньше 2 - не простое")
        return False
    for divisor in range(2, n):
        print(f"Проверяем делитель {divisor}")
        if n % divisor == 0:
            print(f"Нашли делитель {divisor} - число не простое")
            return False
    print("Делителей не найдено - число простое!")
    return True
check_prime(11)
check_prime(9)