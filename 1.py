def two_nums():
    try:
        a = int(input("Введите первое целое число: "))
        b = int(input("Введите второе целое число: "))
    except ValueError:
        print("Я сказал целые числа")
        two_nums()
    else:
        print(f"Поздравляю, вы ввели {a} и {b}")
        print(f"Сумма чисел: {a+b}")
two_nums()