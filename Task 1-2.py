import math
import cmath
import re

def action_1():
    print("Вы ввели цифру 1")
    a = float(input("Введите длину первого катета: "))
    b = float(input("Введите длину второго катета: "))
    s = 0.5 * a * b
    print("Площадь треугольника равна", s)

def action_2():
    print("Вы ввели цифру 2")
    n = 1388  
    m = 7     
    row = (n // m) - 1
    col = (n % m) - 1
    print("Элемент под номером 1388 находится в строке", row, "и столбце", col)

def action_3():
    print("Вы ввели цифру 3")
    radius = 1
    volume = (4 / 3) * math.pi * radius ** 3
    print("Объем шара радиуса 1:", volume)
    # Проверка равенства e^(i*pi) = -1
    result = cmath.exp(1j * math.pi) + 1
    if abs(result) < 1e-9:
        print("Равенство верно.")
    else:
        print("Равенство неверно.")

def action_4():
    print("Вы ввели цифру 4")
    a = 4
    alpha = 60  # угол в градусах
    b = a * math.tan(math.radians(alpha))
    S = 0.5 * a * b
    print("Площадь треугольника равна:", S)

def action_5():
    print("Вы ввели цифру 5")
    e = float(input("Введите эксцентриситет: "))
    if e == 0:
        print("Круговая орбита")
    elif 0 < e < 1:
        print("Эллиптическая орбита")
    elif e == 1:
        print("Параболическая орбита")
    elif e > 1:
        print("Гиперболическая орбита")
    elif e == math.inf:
        print("Прямая орбита")
    else:
        print("Ошибка: неверное значение эксцентриситета")

def action_6():
    print("Вы ввели цифру 6")
    k = 0
    sum = 0
    term = 1
    while term > 1e-10:  # задаем условие остановки суммирования
        sum += term
        k += 1
        term = 1 / math.factorial(k)
    print(f"Сумма ряда = {sum}")
    print(f"Приближенное значение числа e = {math.e}")

def action_7():
    print("Вы ввели цифру 7")
    e = 1e-10  # заданная точность
    sum = 0
    k = 1
    diff = abs(sum - math.pi**2/12)

    while diff >= e:
        sum += (-1)**(k+1)/k**2
        k += 1
        diff = abs(sum - math.pi**2/12)
    print(f"Количество членов ряда: {k}")

def action_8():
    print("Вы ввели цифру 8")
    for n in range(0, 20, 5):
        for z in range(0, 110, 10):
            filename = f"results_n{n:02d}_z{z:03d}.bin"
            print(filename)

def action_9():
    print("Вы ввели цифру 9")
    s = 'Съешь ещё этих мягких французских булок, да выпей же чаю'
    result = s[22:32] + s[48] + ' ' + s[8] + s[50] + ' ' + s[0:3] + s[36] + ' ' + s[53] + s[35:39]
    print(result)

def action_10():
    print("Вы ввели цифру 10")
    s = 'results_n00_z000.bin\nresults_n00_z010.bin\nresults_n00_z020.bin\nresults_n00_\
        z030.bin\nresults_n00_z040.bin\nresults_n00_z050.bin\nresults_n00_z060.bin\nresults_n00_\
            z070.bin\nresults_n00_z080.bin\nresults_n00_z090.bin\nresults_n00_z100.bin\nresults_n05_\
                z000.bin\nresults_n05_z010.bin\nresults_n05_z020.bin\nresults_n05_z030.bin\nresults_n05_\
                    z040.bin\nresults_n05_z050.bin\nresults_n05_z060.bin\nresults_n05_z070.bin\nresults_n05_\
                        z080.bin\nresults_n05_z090.bin\nresults_n05_z100.bin\nresults_n10_z000.bin\nresults_n10_\
                            z010.bin\nresults_n10_z020.bin\nresults_n10_z030.bin\nresults_n10_z040.bin\nresults_n10_\
                                z050.bin\nresults_n10_z060.bin\nresults_n10_z070.bin\nresults_n10_z080.bin\nresults_n10_\
                                    z090.bin\nresults_n10_z100.bin\nresults_n15_z000.bin\nresults_n15_z010.bin\nresults_n15_\
                                        z020.bin\nresults_n15_z030.bin\nresults_n15_z040.bin\nresults_n15_z050.bin\nresults_n15_\
                                            z060.bin\nresults_n15_z070.bin\nresults_n15_z080.bin\nresults_n15_z090.bin\nresults_n15_z100.bin\n'
    pattern = r"n(\d{2})_z(\d{3})"
    matches = re.findall(pattern, s)
    for n, z in matches:
        print(f"({n}, {z})")

def action_11():
    print("Вы ввели цифру 11")
    text = "В худой котомк поклав ржаное хлебо,\n\
        Я ухожу туда, где птичья звон.\n\
            И вижу над собою синий небо,\n\
                Косматый облак и высокий крон.\n\n\
                    Я дома здесь. Я здесь пришел не в гости.\n\
                        Снимаю кепк, одетый набекрень.\n\
                            Веселый птичк, помахивая хвостик,\n\
                                Высвистывает мой стихотворень.\n\n\
                                    Зеленый травк ложится под ногами,\n\
                                        И сам к бумаге тянется рука.\n\
                                            И я шепчу дрожащие губами:\n\
                                                «Велик могучим русский языка!»\n"
    words = text.replace(',', '').replace('.', '').replace('«', '').replace('»', '').split()
    lst = []
    for word in words:
        length = len(word)
        vowels = sum([1 for letter in word if letter in 'аеёиоуыэюя'])
        lst.append((word, length, vowels))
    print(lst)

x = int(input("Введите цифру от 1 до 11: "))

match x:
    case 1:
        action_1()
    case 2:
        action_2()
    case 3:
        action_3()
    case 4:
        action_4()
    case 5:
        action_5()
    case 6:
        action_6()
    case 7:
        action_7()
    case 8:
        action_8()
    case 9:
        action_9()
    case 10:
        action_10()
    case 11:
        action_11()
    case _:
        print("Вы ввели некорректное значение")