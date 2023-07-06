def task():
    from functools import reduce
    try:
        # Запрашиваем строку
        string = input()
        # Из строки делам список по пробелам(split) попутно удаляем весь мусор по бокам(strip)
        list_string = string.strip().split()
        # Проверяем 2 элемент и 4 элемент чтоб задать условие
        # 1 условие проверяет на знак "+"
        if list_string[1] == "+" and list_string[3] == "=":
            # Удаляем не числовые значения
            list_string = [
                x for x in list_string if not x.startswith("+") and not x.startswith("=")
            ]
            # Преобразовываем строки в числа
            list_string = list(map(int, list_string))
            # С помощью функции reduce вычисляем сумму
            sum_string = reduce(lambda x, y: x + y, list_string)
            # Отправляем ответ
            print(f"Ответ: {sum_string}")
        # 2 условие проверяет на знак "+"
        elif list_string[1] == "-" and list_string[3] == "=":
            # Удаляем не числовые значения
            list_string = [
                x for x in list_string if not x.startswith("-") and not x.startswith("=")
            ]
            # Преобразовываем строки в числа
            list_string = list(map(int, list_string))
            # С помощью функции reduce вычисляем разность
            sum_string = reduce(lambda x, y: x - y, list_string)
            # Отправляем ответ
            print(f"Ответ: {sum_string}")
        # 3 условие проверяет на знак "/"
        elif list_string[1] == "/" and list_string[3] == "=":
            # Удаляем не числовые значения
            list_string = [
                x for x in list_string if not x.startswith("/") and not x.startswith("=")
            ]
            # Преобразовываем строки в числа
            list_string = list(map(int, list_string))
            # С помощью функции reduce вычисляем частное
            sum_string = reduce(lambda x, y: x / y, list_string)
            # Отправляем ответ
            print(f"Ответ: {sum_string}")
        # 4 условие проверяет на знак "*"
        elif list_string[1] == "*" and list_string[3] == "=":
            # Удаляем не числовые значения
            list_string = [
                x for x in list_string if not x.startswith("*") and not x.startswith("=")
            ]
            # Преобразовываем строки в числа
            list_string = list(map(int, list_string))
            # С помощью функции reduce вычисляем  произведение
            sum_string = reduce(lambda x, y: x * y, list_string)
            # Отправляем ответ
            print(f"Ответ: {sum_string}")
        # Если условие будет неизвестное
        else:
            raise ValueError("Неизвестная операция")


    except ValueError as e:
        print("Ошибка: ", e)


# task()