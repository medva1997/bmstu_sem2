import math


# Печать всей таблицы
def PrintTable(arrtable):
    for i in range(len(arrtable)):
        PrintTableLine(arrtable[i])


# Печать строки таблицы
def PrintTableLine(arrLine):
    prformat = "{:^12}|"
    separator = '|'
    endline = ' '
    for i in range(len(arrLine)):
        print(prformat.format(arrLine[i]), sep=separator, end=endline)
    print()


def FuncZero(x):
    return 0


def ProizZero(x):
    return 0;


def Func(x):
    return x * x - 4


def ProizF(x):
    return 2 * x


def Func1(x):
    return math.sin(x)


def ProizF1(x):
    # print(('wor'))
    return math.cos(x)

def Func4(x):
    return math.cos(x)


def ProizF4(x):
    # print(('wor'))
    return math.sin(x)


def Func2(x):
    if x == 0:
        return 1.0
    return math.sin(x) / x


def ProizF2(x):
    if x == 0:
        return 0.0
    return (x * math.cos(x) - math.sin(x)) / (x * x)


def Alp(poizfunc, x):
    if x == 0:
        x = 0.0001
    return (1 / poizfunc(x))


def Func3(x):
    return -math.sin(x) + 1.5


def ProizF3(x):
    return -math.sin(x)


# Вычесления итерациями, func2 - функция с которой ищем коррни.
def IteratorFunc(left, n, epsx, epsy, func1, poizfunc1, func2, l):
    k = 0
    x = left
    D = epsx
    while (abs((func2(x) - func1(x))) > epsy) or (D >= epsx):
        Xpr = x
        x = Xpr - poizfunc1(Xpr) * (func1(Xpr) - func2(Xpr))
        D = abs(x - Xpr)
        k += 1
        if (k > n):
            break
    return k, x


def SmallCounter(left, right, n, epsx, epsy, id, func1, poizfunc1, func2):
    out = []
    k = 1

    l = 0

    if (func1(left) * func1(right) > 0):
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('-')
        out.append('-')
        out.append('-')
        out.append('2')
        return []

    if (abs(func1(left) - func2(left)) < epsy):
        x = left
        print(abs(func1(left) - func2(left)))

        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('{:2.5f}'.format(x))
        out.append('{:2.4e}'.format(func1(x)))
        out.append(k)
        out.append("0")
        return out

    k, x = IteratorFunc(left, n, epsx, epsy, func1, poizfunc1, func2, l)

    if (x < left):
        t, x = IteratorFunc((left + right) / 2, n, epsx, epsy, func1, poizfunc1, func2, l)
        k = k + t

    if (x < left):
        t, x = IteratorFunc(right, n, epsx, epsy, func1, poizfunc1, func2, l)
        k = k + t

    if (x > right):
        t, x = IteratorFunc((left + right) / 2, n, epsx, epsy, func1, poizfunc1, func2, l)
        k = k + t

    if (x > right):
        t, x = IteratorFunc(right, n, epsx, epsy, func1, poizfunc1, func2, l)
        k = k + t

    if ((x < right) and (x > left)):
        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        if (k < n * 6):
            out.append('{:2.5f}'.format(x))
            out.append('{:2.4e}'.format(func1(x)))
            out.append(k)
            out.append("0")

        else:
            out.append(':-(')
            out.append(':-(')
            out.append(':-(')
            out.append('1')
        return out
    return []


def integrare_by_bull(a, b, n, func):
    if ((n) % 2 == 0):
        return bulean(a, b, func, n)
    else:
        print("Метод Буля не работает, для нечетного колества интервалов. Вычесление невозможно.")
    return 0


def bulean(a, b, func, n):
    step = (b - a) / (4 * n)
    pos = a
    boleanrez = 0
    for i in range(0, n):
        boleanrez += 2 * step / 45 * smallbool(pos, step, func)
        pos += step * 4
    return boleanrez


def smallbool(pos, step, func):
    ln = 7 * func(pos)
    ln += 32 * func(pos + step)
    ln += 12 * func(pos + step * 2)
    ln += 32 * func(pos + step * 3)
    ln += 7 * func(pos + step * 4)
    return ln


def trapeze(a, b, func, n, eps):
    trapezeres = 0
    step = (b - a) / n
    pos = a
    while (abs(pos - b) > eps):
        trapezeres += trapezecount(pos, step)
        print(pos, trapezecount(pos, step))
        pos += step
    return trapezeres


def trapezecount(pos, step, func):
    left = pos
    right = pos + step
    S = (func(left) + func(right)) / 2 * step
    return S


def tree(a, b, n, func):
    step = (b - a) / n
    summ = 0
    pos = a
    while (pos < b):
        summ += 3 * step / 8 * (func(pos) + func(pos + 3 * step) + 3 * func(pos + step) + 3 * func(pos + 2 * step))
        pos += step * 3
    return summ
