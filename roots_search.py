import math
import pylab
from matplotlib import mlab

def Func(x):
    return math.sin(x)

def Func1(x):
    return 0;

def ProizF(x):
    return math.cos(x)

#====================================ИТЕРАЦИЙ (iteration)=========================================

# Вызов метода итераций для каждого отрезка
def CounterIteration(a,b,h,n,epsy,epsx,table,f1, proizF1, f2):
    for i in range(int((b - a) / h)):
        z = Interation(a + i * h, a + (i + 1) * h, n, epsx, epsy, len(table), f1, proizF1, f2)
        if (z != []):
            table.append(z)
    z = Interation(a + int((b - a) // h) * h, b, n, epsx, epsy, len(table), f1, proizF1, f2)
    if (z != []):
        table.append(z)
# поиск корня методами итерацый на учатске. часть 1 из 2
# Вычесления итерациями, func2 - функция с которой ищем коррни.
def IteratorFunc(left, n, epsx, epsy, func1, poizfunc1, func2):
    k = 0
    x = left
    D = epsx
    while (abs((func2(x) - func1(x))) > epsy) or (D >= epsx):
        Xpr = x
        x = Xpr - 1/poizfunc1(Xpr) * (func1(Xpr) - func2(Xpr))
        D = abs(x - Xpr)
        k += 1
        if (k > n):
            break
    return k, x
# поиск корня методами итерацый на учатске. часть 1 из 2
def Interation(left, right, n, epsx, epsy, id, func1, poizfunc1, func2):
    #Часть таблицы
    out = []

    k = 1
    l = 0
    #Нет корней на участке
    if (func1(left) * func1(right) > 0):
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('-')
        out.append('-')
        out.append('-')
        out.append('2')
        return []

    #формирование таблицы
    if (abs(func1(left) - func2(left)) < epsy):
        x = left
        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('{:2.5f}'.format(x))
        out.append('{:2.4e}'.format(func1(x)))
        out.append(k)
        out.append("0")
        return out
    # Поиск корня
    k, x = IteratorFunc(left, n, epsx, epsy, func1, poizfunc1,func2)

    if (x < left):
        t, x = IteratorFunc((left + right) / 2, n, epsx, epsy, func1, poizfunc1,func2)
        k = k + t

    if (x < left):
        t, x = IteratorFunc(right, n, epsx, epsy, func1, poizfunc1,func2)
        k = k + t

    if (x > right):
        t, x = IteratorFunc((left + right) / 2, n, epsx, epsy, func1, poizfunc1,func2)
        k = k + t

    if (x > right):
        t, x = IteratorFunc(right, n, epsx, epsy, func1, poizfunc1,func2)
        k = k + t

    # Формирование таблицы
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

#====================================Хорд (Xord)=========================================

# Вызов метода хорд для каждого отрезка
def CounterXord(a,b,h,n,epsy,epsx,table,f1, proizF1, f2):
    for i in range(int((b - a) / h)):
        z = Xord(a + i * h, a + (i + 1) * h, n, epsx, epsy, len(table), f1, f2)
        if (z != []):
            table.append(z)
    z = Xord(a + int((b - a) // h) * h, b, n, epsx, epsy, len(table), f1, f2)
    if (z != []):
        table.append(z)
# поиск корня методами xord на учатске. часть 1 из 2
def Xord(left, right, n, epsx, epsy, id, func1, func2):
    #Часть таблицы
    out = []
    k = 1
    l = 0
    #Нет корней на участке
    if (func1(left) * func1(right) > 0):
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('-')
        out.append('-')
        out.append('-')
        out.append('2')
        return []

    #формирование таблицы
    if (abs(func1(left) - func2(left)) < epsy):
        x = left
        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('{:2.5f}'.format(x))
        out.append('{:2.4e}'.format(func1(x)))
        out.append(k)
        out.append("0")
        return out
    # Поиск корня
    k, x = XordStaticA(left,right, n, epsx, epsy, func1,func2)


    # Формирование таблицы
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

def XordStaticA(left,right, n, epsx, epsy, func1, func2):
    k = 0
    x = right
    D = epsx
    while (abs((func2(x) - func1(x))) > epsy) or (D >= epsx):
        Xpr = x
        x = Xpr -func1(Xpr)/(func1(Xpr)-func1(left))*(Xpr-left)
        D = abs(x - Xpr)
        k += 1
        if (k > n):
            break
    return k, x
#НЕ РАБОТАЕТ ИСПОЛЬЗОВАТЬ А
def XordStaticB(left,right, n, epsx, epsy, func1,  func2):
    k = 0
    x = left
    D = epsx
    while (abs((func2(x) - func1(x))) > epsy) or (D >= epsx):
        Xpr = x
        x = Xpr -func1(Xpr)/(func1(right)-func1(Xpr))*(right-Xpr)
        D = abs(x - Xpr)
        k += 1
        if (k > n):
            break
    return k, x


#====================================Половинного деления(middle)=========================================
# Вызов метода хорд для каждого отрезка
def CounterMiddle(a,b,h,n,epsy,epsx,table,f1, proizF1, f2):
    for i in range(int((b - a) / h)):
        z = Middle(a + i * h, a + (i + 1) * h, n, epsx, epsy, len(table), f1, f2)
        if (z != []):
            table.append(z)
    z = Middle(a + int((b - a) // h) * h, b, n, epsx, epsy, len(table), f1, f2)
    if (z != []):
        table.append(z)
# поиск корня методами xord на учатске. часть 1 из 2
def Middle(left, right, n, epsx, epsy, id, func1, func2):
    #Часть таблицы
    out = []
    k = 1
    l = 0
    #Нет корней на участке
    if (func1(left) * func1(right) > 0):
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('-')
        out.append('-')
        out.append('-')
        out.append('2')
        return []

    #формирование таблицы
    if (abs(func1(left) - func2(left)) < epsy):
        x = left
        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('{:2.5f}'.format(x))
        out.append('{:2.4e}'.format(func1(x)))
        out.append(k)
        out.append("0")
        return out
    # Поиск корня
    k, x = XMiddle(left,right, n, epsx, epsy, func1,func2)


    # Формирование таблицы
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

def XMiddle(left,right, n, epsx, epsy, func1, func2):
    k = 0
    xl = left
    xr=right
    xm=(xl+xr)/2
    D = epsx
    while (abs((func2(xm) - func1(xm))) > epsy) or (D >= epsx):
        xm=(xl+xr)/2
        Xpr=xm
        if(func1(xm)*func1(xl)<0) :
            xr=xm
        else:
            xl=xm
        D = abs(xm - Xpr)
        k += 1
        if (k > n):
            break
    return k, xm

#====================================Стеффансона (Steffanson)=========================================

def CounterSTEF(a,b,h,n,epsy,epsx,table,f1, proizF1, f2):
    for i in range(int((b - a) / h)):
        z = STEF(a + i * h, a + (i + 1) * h, n, epsx, epsy, len(table), f1, f2)
        if (z != []):
            table.append(z)
    z = STEF(a + int((b - a) // h) * h, b, n, epsx, epsy, len(table), f1, f2)
    if (z != []):
        table.append(z)

def STEF(left, right, n, epsx, epsy, id, func1, func2):
    #Часть таблицы
    out = []
    k = 1
    l = 0
    #Нет корней на участке
    if (func1(left) * func1(right) > 0):
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('-')
        out.append('-')
        out.append('-')
        out.append('2')
        return []

    #формирование таблицы
    if (abs(func1(left) - func2(left)) < epsy):
        x = left
        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('{:2.5f}'.format(x))
        out.append('{:2.4e}'.format(func1(x)))
        out.append(k)
        out.append("0")
        return out
    # Поиск корня
    k, x = XSTEF(left,right, n, epsx, epsy, func1,func2)
    k, x = XSTEF(left,right, n, epsx, epsy, func1,func2)

    if (x < left):
        t, x = XSTEF((left + right) / 2, right, n, epsx, epsy, func1,func2)
        k = k + t

    if (x < left):
        t, x = XSTEF(right, right, n, epsx, epsy, func1,func2)
        k = k + t

    if (x > right):
        t, x = XSTEF((left + right) / 2,right, n, epsx, epsy, func1,func2)
        k = k + t

    if (x > right):
        t, x = XSTEF(right, right, n, epsx, epsy, func1,func2)
        k = k + t

    # Формирование таблицы
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

def XSTEF(left,right, n, epsx, epsy, func1, func2):
    k = 0
    x = left
    D = epsx
    while (abs((func2(x) - func1(x))) > epsy) or (D >= epsx):
        Xpr = x
        x = Xpr - func1(Xpr)/(func1(Xpr+func1(Xpr))-func1(Xpr))*func1(Xpr)
        D = abs(x - Xpr)
        k += 1
        if (k > n):
            break
    return k, x

#====================================Упрощенного(модифицированного) Ньютона(Modificate easy Newton=========================================


def CounterEasyNewton(a,b,h,n,epsy,epsx,table,f1, proizF1, f2):
    for i in range(int((b - a) / h)):
        z = EasyNewton(a + i * h, a + (i + 1) * h, n, epsx, epsy, len(table), f1, proizF1, f2)
        if (z != []):
            table.append(z)
    z = EasyNewton(a + int((b - a) // h) * h, b, n, epsx, epsy, len(table), f1, proizF1, f2)
    if (z != []):
        table.append(z)

def EasyNewton(left, right, n, epsx, epsy, id, func1, poizfunc1, func2):
    #Часть таблицы
    out = []

    k = 1
    l = 0
    #Нет корней на участке
    if (func1(left) * func1(right) > 0):
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('-')
        out.append('-')
        out.append('-')
        out.append('2')
        return []

    #формирование таблицы
    if (abs(func1(left) - func2(left)) < epsy):
        x = left
        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('{:2.5f}'.format(x))
        out.append('{:2.4e}'.format(func1(x)))
        out.append(k)
        out.append("0")
        return out
    # Поиск корня
    k, x = XEasyNewton(left,right, n, epsx, epsy, func1, poizfunc1,func2)



    # Формирование таблицы
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

def XEasyNewton(left,right, n, epsx, epsy, func1, poizfunc1, func2):
    k = 0
    x = (left+right)/2
    D = epsx
    proiz=poizfunc1(x)

    while (abs((func2(x) - func1(x))) > epsy) or (D >= epsx):
        Xpr = x
        x = Xpr - func1(Xpr)/proiz
        D = abs(x - Xpr)
        k += 1
        if (k > n):
            break
    return k, x

#==================================== Ньютона (Newton)=========================================


def CounterNewton(a,b,h,n,epsy,epsx,table,f1, proizF1, f2):
    for i in range(int((b - a) / h)):
        z = Newton(a + i * h, a + (i + 1) * h, n, epsx, epsy, len(table), f1, proizF1, f2)
        if (z != []):
            table.append(z)
    z = Newton(a + int((b - a) // h) * h, b, n, epsx, epsy, len(table), f1, proizF1, f2)
    if (z != []):
        table.append(z)

def Newton(left, right, n, epsx, epsy, id, func1, poizfunc1, func2):
    #Часть таблицы
    out = []

    k = 1
    l = 0
    #Нет корней на участке
    if (func1(left) * func1(right) > 0):
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('-')
        out.append('-')
        out.append('-')
        out.append('2')
        return []

    #формирование таблицы
    if (abs(func1(left) - func2(left)) < epsy):
        x = left
        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('{:2.5f}'.format(x))
        out.append('{:2.4e}'.format(func1(x)))
        out.append(k)
        out.append("0")
        return out
    # Поиск корня
    k, x = XEasyNewton(left,right, n, epsx, epsy, func1, poizfunc1,func2)



    # Формирование таблицы
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

def XNewton(left,right, n, epsx, epsy, func1, poizfunc1, func2):
    k = 0
    x = (left+right)/2
    D = epsx


    while (abs((func2(x) - func1(x))) > epsy) or (D >= epsx):
        Xpr = x
        x = Xpr - func1(Xpr)/poizfunc1(x)
        D = abs(x - Xpr)
        k += 1
        if (k > n):
            break
    return k, x

#==================================== Секущих (Sekyshix)=========================================


def CounterSecant(a,b,h,n,epsy,epsx,table,f1, proizF1, f2):
    for i in range(int((b - a) / h)):
        z = Secant(a + i * h, a + (i + 1) * h, n, epsx, epsy, len(table), f1, proizF1, f2)
        if (z != []):
            table.append(z)
    z = Secant(a + int((b - a) // h) * h, b, n, epsx, epsy, len(table), f1, proizF1, f2)
    if (z != []):
        table.append(z)

def Secant(left, right, n, epsx, epsy, id, func1, poizfunc1, func2):
    #Часть таблицы
    out = []

    k = 1
    l = 0
    #Нет корней на участке
    if (func1(left) * func1(right) > 0):
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('-')
        out.append('-')
        out.append('-')
        out.append('2')
        return []

    #формирование таблицы
    if (abs(func1(left) - func2(left)) < epsy):
        x = left
        out.append(id)
        out.append('{:3.5g}'.format(left))
        out.append('{:3.5g}'.format(right))
        out.append('{:2.5f}'.format(x))
        out.append('{:2.4e}'.format(func1(x)))
        out.append(k)
        out.append("0")
        return out
    # Поиск корня
    k, x = XSecant(left,right, n, epsx, epsy, func1, poizfunc1,func2)



    # Формирование таблицы
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

def XSecant(left,right, n, epsx, epsy, func1, poizfunc1, func2):
    k = 0
    x = (left+right)/2
    D = epsx
    Xprpr=left
    Xpr=right

    while (abs((func2(x) - func1(x))) > epsy) or (D >= epsx):
        Xprpr=Xpr
        Xpr = x
        x = Xpr - (Xpr-Xprpr)/(func1(Xpr)-func1(Xprpr))*func1(Xpr)
        D = abs(x - Xpr)
        k += 1
        if (k > n):
            break
    return k, x

#====================================ИНТЕНРИРОВАНИЕ (integrate)===============================
# Интегрирование булем часть 1 из 3
def integrare_by_bull(a, b, n, func):
    if ((n) % 2 == 0):
        return bulean(a, b, func, n)
    else:
        print("Метод Буля не работает, для нечетного колества интервалов. Вычесление невозможно.")
    return 0
# Интегрирование булем часть 2 из 3
def bulean(a, b, func, n):
    step = (b - a) / (4 * n)
    pos = a
    boleanrez = 0
    for i in range(0, n):
        boleanrez += 2 * step / 45 * smallbool(pos, step, func)
        pos += step * 4
    return boleanrez
# Интегрирование булем часть 3 из 3
def smallbool(pos, step, func):
    ln = 7 * func(pos)
    ln += 32 * func(pos + step)
    ln += 12 * func(pos + step * 2)
    ln += 32 * func(pos + step * 3)
    ln += 7 * func(pos + step * 4)
    return ln

#====================================ОБЩЕЕ (other)===============================
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
# Ввод всего.
def MainInput():
    manualinput = True
    manualsmallintput = True

    manualinput = False
    manualsmallintput = False

    if (manualinput == True):
        a = float(input("Введите значение левой границы: "))
        b = float(input("Введите значение правой границы: "))
        h = float(input("Введите длину шага: "))
    else:
        a = -20
        b = 20
        h = 3.14

    if (manualsmallintput == True):
        epsx = float(input("Введите значение погрешности по x: "))
        epsy = float(input("Введите значение погрешности по y: "))
        n = int(input(("Введите  максимальное количество итераций: ")))
    else:
        epsy = 0.00001
        epsx = 0.00001
        n = 100
    return a, b, h, n, epsx, epsy

def Draw(func1, func2):
    # генирация точек графика
    xlist = mlab.frange(a, b, 0.01)
    ylist = [func1(x) for x in xlist]
    ylist2 = [func2(x) for x in xlist]

    # Генирирум ось
    y0 = [0 for x in xlist]
    pylab.plot(xlist, ylist)
    #pylab.plot(xlist, y0, label='line1', color='blue')
    pylab.plot(xlist, ylist2, label='$sin(x)/x)$', color='red')
    pylab.legend()

    # Включаем рисование сетки
    pylab.grid(True)

    pylab.fill_between(xlist, ylist, ylist2, color='green', alpha=0.25)
    # если мало разбиений, то переопереляем сетку под шаг
    if ((round((b - a) / h)) < 25):
        pylab.xticks([a + i * h for i in range(round((b - a) / h) + 1)])
    # рисуем корни, промерка того что корень не содержит ошибок
    for i in range(1, len(table)):
        if (table[i][4] != ':-('):
            pylab.scatter(table[i][3], table[i][4])

    # Рисуем фогрму с графиком
    pylab.show()

a, b, h, n, epsx, epsy = MainInput()
ln = ['N', 'A', 'B', 'X', 'F(x)', 'итераций', 'код ошибки']
table = []
table.append(ln)
CounterSTEF(a, b, h, n, epsx, epsy,table,Func,ProizF,Func1)
PrintTable(table)

