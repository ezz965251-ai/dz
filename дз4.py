def print_line(len_line, dir_line, char_line):
    print(f"Рисуем линию: длина={len_line}, направление={dir_line}, символ='{char_line}'")
    if dir_line == "horizontal" or dir_line == "h":
        print("Горизонтальная линия:")
        line = ""
        for i in range(len_line):
            line += char_line + " "
        print(line)
    elif dir_line == "vertical" or dir_line == "v":
        print("Вертикальная линия:")
        for i in range(len_line):
            print(char_line)
    else:
        print("Неизвестное направление! Используйте 'h' или 'v'")
print_line(4, 'h', '-')
print_line(4, 'v', '|')