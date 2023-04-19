import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def action_1():
    print("Вы ввели цифру 1")
    # массив действительных чисел
    a = np.pi * (2 ** -np.arange(0, 11))
    print("Массив a:", a)
    print("Форма массива a:", a.shape)
    print("Размер занимаемой памяти a:", a.nbytes, "байт")
    
    # массив True/False
    b = np.arange(10, 101) % 5 == 0
    print("Массив b:", b)
    print("Форма массива b:", b.shape)
    print("Размер занимаемой памяти b:", b.nbytes, "байт")

    # двумерный массив комплексных чисел
    k, m = np.meshgrid(np.arange(11), np.arange(11))
    c = 1.5 * k + 2.5j * m
    print("Массив c:", c)
    print("Форма массива c:", c.shape)
    print("Размер занимаемой памяти c:", c.nbytes, "байт")

def action_2():
    print("Вы ввели цифру 2")
    # Задание 1
    seq = np.arange(1, 101) / 30
    # Задание 2
    arr = np.random.uniform(low=np.pi, high=10*np.pi, size=(10, 10))
    # Задание 3
    arr_int = arr.astype(int)
    # Задание 4
    indices = np.random.choice(np.arange(100), size=10, replace=False)
    random_elements = indices.tolist()
    print("Задание 1:")
    print(seq)
    print(seq.shape)
    print(seq.nbytes)

    print("\nЗадание 2:")
    print(arr)
    print(arr.shape)
    print(arr.nbytes)

    print("\nЗадание 3:")
    print(arr_int)
    print(arr_int.shape)
    print(arr_int.nbytes)

    print("\nЗадание 4:")
    print(random_elements)

def action_3():
    print("Вы ввели цифру 3")
    arr = np.array([range(5, 10)]).T * range(1, 4)
    print(arr)
#     range(5, 10) создает последовательность чисел от 5 до 9 включительно.
#     [range(5, 10)] создает список, содержащий эту последовательность чисел.
#     np.array([range(5, 10)]) преобразует этот список в одномерный массив NumPy, который содержит числа от 5 до 9.
#     .T выполняет транспонирование массива, превращая его в столбец. В результате мы получаем массив-столбец с элементами от 5 до 9.
#     range(1, 4) создает последовательность чисел от 1 до 3 включительно.
#     np.array([range(5, 10)]).T * range(1, 4) выполняет поэлементное умножение между столбцом массива [5, 6, 7, 8, 9] и вектором [1, 2, 3]. 
#     Но так как массив-столбец имеет форму (5, 1), а вектор имеет форму (3,), то происходит broadcasting (броадкастинг), и каждый элемент массива-столбца умножается на соответствующий элемент вектора. 
#     В результате получается двумерный массив размером (5, 3) с элементами, равными произведениям чисел от 5 до 9 на числа от 1 до 3:

def action_4():
    print("Вы ввели цифру 4")
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    result = arr[:, [1, 3]]
    print(result)
    x = np.arange(0, 11)
    y = np.arange(0, 11)
    # создание массивов x и y с помощью meshgrid
    X, Y = np.meshgrid(x, y)
    # создание массива значений x + iy
    Z = X + 1j * Y
    # выбор элементов с модулем, не превышающим 7
    result = Z[np.abs(Z) <= 7]
    print(result)
#     Первые две строки кода создают одномерные массивы x и y с числами от 0 до 10 включительно.
#     Третья и четвертая строки создают двумерные массивы X и Y с помощью функции meshgrid. Эти массивы представляют собой сетку точек, где каждая точка имеет координаты (x, y).
#     Пятая строка создает массив значений x + iy, используя броадкастинг.
#     Шестая строка выбирает только элементы этого массива, чей модуль не превышает 7. Используя np.abs(Z) <= 7, мы получаем логический массив той же формы, что и массив Z, 
#     содержащий True для элементов, модуль которых не превышает 7, и False для всех остальных элементов. Затем мы используем этот логический массив 
#     в качестве маски для выбора элементов массива Z с помощью операции `Z[np.abs(Z) <= 7

def action_5():
    print("Вы ввели цифру 5")
    #%%
    import numpy as np
    import matplotlib.pyplot as plt
    t = np.linspace(0, 12 * np.pi, 2000)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.power(np.sin(t/12), 5))
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.power(np.sin(t/12), 5))
    plt.plot(x, y)
    plt.show()
# %%

def action_6():
    print("Вы ввели цифру 6")
    a = np.array([0, 1, 2, 3, 4, 5])
    b = np.array([10, 11, 12, 13, 14, 15])
    # используем метод reshape для объединения двух одномерных массивов в двумерный
    c = np.concatenate([a, b]).reshape((2, 6))
    print(c)

def action_7():
    print("Вы ввели цифру 7")
    # задаем координаты точек ломаной линии
    x = np.array([0, 1, 3, 4, 6])
    y = np.array([0, 2, 1, 3, 2])
    # вычисляем разности между соседними точками
    dx = np.diff(x)
    dy = np.diff(y)
    # вычисляем длину каждого отрезка
    lengths = np.sqrt(dx**2 + dy**2)
    # вычисляем сумму длин отрезков
    total_length = np.sum(lengths)
    print(total_length)

def action_8():
    print("Вы ввели цифру 8")
    #%%
    import numpy as np
    import matplotlib.pyplot as plt
    N = 8  # Размер доски
    M = 40  # Размер ячейки
    # Создаем массив с черно-белыми ячейками
    board = np.zeros((N*M, N*M))
    for i in range(N):
        for j in range(N):
            if (i+j) % 2 == 0: # Если четная, то клетка окрашивается в черный
                board[i*M:(i+1)*M, j*M:(j+1)*M] = 1 # этот подмассив будет заполнен 1, если i+j является четным числом, и 0, если i+j является нечетным числом
    # Выводим изображение доски
    plt.imshow(board, cmap='binary')
    plt.axis('off')
    plt.show()

#%%

def action_9():
    print("Вы ввели цифру 9")

def action_10():
    print("Вы ввели цифру 10")

def action_11():
    print("Вы ввели цифру 11")

def action_12():
    print("Вы ввели цифру 12")

x = int(input("Введите цифру от 1 до 12: "))

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
    case 12:
        action_12()
    case _:
        print("Вы ввели некорректное значение")

