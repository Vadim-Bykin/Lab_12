#6. Вычислить сумму знакопеременного ряда |х(n-1)|/(n-1)!, где х-матрица ранга к
# (к и матрица задаются случайным образом), n - номер слагаемого.
# Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
# У алгоритма д.б. линейная сложность. Знак первого слагаемого  -.

import random
import numpy as np

# создание матрицы
def make_matrix(t):
    k = random.randint(2, 6)
    n = []
    for i in range(k):
        n.append([])
        for j in range(k):
            n[i].append(random.choice([-1, 1]))
    matrix = np.array(n)
    if abs(np.linalg.det(n)) == 0:
        return make_matrix(t)
    else:

        return matrix

# функция факториала
def fac(n):
    answer = 1
    for i in range(1, n):
        answer *= i
    return answer

# функция для подсчёта знакопеременного ряда
def Line(t):
    if t < 0:
        print('Введите положительное число')
        return
    matrix = make_matrix(t)
    print("Начальная матрица: ")
    print(matrix)
    answ = 0.0
    n = 1
    flag = True
    while flag:
        try:
            matrix = matrix * fac(n - 1)
            answ += ((-1) ** n) * (abs(np.linalg.det(matrix)) / fac(n - 1))
            n += 1
            if len(str(answ).split('.')) >= 2:
                if len(str(answ).split('.')[1]) > t:
                    flag = False
                elif str(answ).find('e') != -1:
                    try:
                        flag = (len(str(answ).split('.')[1]) + int(str(answ).split('-')[1])) < t
                    except:
                        flag = (len(str(answ).split('.')[1]) + int(str(answ).split('+')[1])) < t
        except np.core._exceptions.UFuncTypeError:
            print('Числа в матрице вышли слишком большими')
            print('Для повторного запуска напишите новое число:')
            return
    print('финальный вид матрицы:')
    print(matrix)
    print('Сумма знакопеременного ряда |х(n-1)|/(n-1)!:', answ)
    print('Для повторного запуска напишите новое число:')

# запуск программы
while True:
    try:
        Line(int(input('Введите t - кол-во знаков после запятой: ')))
    except ValueError:
        print('Введите число')
