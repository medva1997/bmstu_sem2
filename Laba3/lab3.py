import pylab
import laba3_part2
from matplotlib import mlab

from laba3_func import *


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
        h = 2
    if (manualsmallintput == True):
        epsx = float(input("Введите значение погрешности по x: "))
        epsy = float(input("Введите значение погрешности по y: "))
        n = int(input(("Введите  максимальное количество итераций: ")))
    else:
        epsy = 0.0001
        epsx = 0.0001
        n = 10000
    return a, b, h, n, epsx, epsy


def converter(tb, startline, col1, col2, func):
    tbX = []
    tbY = []
    for i in range(startline, len(tb)):
        if (tb[i][3] != ':-('):
            tbX.append(tb[i][col1])
            tbY.append(func(float(tb[i][col1])))
    return tbX, tbY


def Draw(func1, func2):
    # генирация точек графиков
    xlist = mlab.frange(a, b, 0.01)
    ylist = [func1(x) for x in xlist]
    ylist2 = [func2(x) for x in xlist]
    # Генирирум ось
    y0 = [0 for x in xlist]

    #############################################################
    max1Y = max(ylist)
    min1Y = min(ylist)
    max2Y = max(ylist2)
    min2Y = min(ylist2)
    minmaxarrayY = []
    minmaxarrayX = []
    for i in range(len(ylist)):
        if ((max1Y == ylist[i]) or (min1Y == ylist[i])):
            minmaxarrayY.append(ylist[i])
            minmaxarrayX.append(xlist[i])

    for i in range(len(ylist2)):
        if ((max2Y == ylist2[i]) or (min2Y == ylist2[i])):
            minmaxarrayY.append(ylist2[i])
            minmaxarrayX.append(xlist[i])

    ################################################################
    extremumX, extremumY = converter(korn, 0, 3, 4, func1)
    inflectionX, inflectionY = converter(korn1, 0, 3, 4, func1)
    kornsX, kornsY = converter(table, 1, 3, 4, func1)

    pylab.plot(extremumX, extremumY, 'go', label='extremum', color='red')
    pylab.plot(inflectionX, inflectionY, 'go', label='inflection point', color='yellow')
    pylab.plot(minmaxarrayX, minmaxarrayY, 'go', label='min/max', color='green')
    pylab.plot(kornsX, kornsY, 'go', label='Korn', color='black')

    pylab.plot(xlist, ylist, label='$sin(x)/x$')
    pylab.plot(xlist, y0, color='pink')
    pylab.plot(xlist, ylist2, label='$0.02*x* x - 4$', color='pink')
    pylab.legend()

    # Включаем рисование сетки
    pylab.grid(True)
    xlist1 = mlab.frange(float(table2[0][3]), float(table2[len(table2) - 1][3]), 0.01)
    pylab.fill_between(xlist1, [func1(x) for x in xlist1], [func2(x) for x in xlist1], color='green', alpha=0.25)
    # если мало разбиений, то переопереляем сетку под шаг
    if ((round((b - a) / h)) < 25):
        pylab.xticks([a + i * h for i in range(round((b - a) / h) + 1)])

    print()
    print()
    print("Минимумы и максимумы:")
    print("X", "Y", sep="\t")
    for i in range(len(minmaxarrayY)):
        print('{:3.5g}'.format(minmaxarrayX[i]), '{:3.5g}'.format(minmaxarrayY[i]), sep='\t\t')
    # Рисуем фогрму с графиком
    pylab.show()


def Counter(f1, proizF1, f2):
    tb = []
    for i in range(int((b - a) / h)):
        z = laba3_part2.SmallCounter(a + i * h, a + (i + 1) * h, n, epsx, epsy, len(tb) + 1, f1, proizF1, f2)
        if (z != []):
            tb.append(z)
    z = laba3_part2.SmallCounter(a + int((b - a) // h) * h, b, n, epsx, epsy, len(table), f1, proizF1, f2)
    if (z != []):
        tb.append(z)
    return tb


a, b, h, n, epsx, epsy = MainInput()

ln = ['N', 'A', 'B', 'X', 'F(x)', 'итераций', 'код ошибки']
table = []
korn = []
korn1 = []
table2 = []
table.append(ln)
ln = ['A', 'B', 'X', 'F(x)', 'итераций', 'код ошибки']
# korn.append(ln)

table2 = Counter(Func1, ProizF1, Func3)
table1 = Counter(Func1, ProizF1, Func2)
table += table2 + table1

korn = Counter(ProizF1, Proiz2F1, Func2)
korn1 = Counter(Proiz2F1, Proiz3F1, Func2)
laba3_part2.PrintTable(table)
print()
print("Экстремему")
laba3_part2.PrintTable(korn)
print()
print("Перегибы")
laba3_part2.PrintTable(korn1)
# laba3_part2.PrintTable(korn)
s = 0

for i in range(len(table2) - 1):
    temp = laba3_part2.integrare_by_bull(float(table2[i][3]), float(table2[i + 1][3]), 100, Func3)
    temp1 = laba3_part2.integrare_by_bull(float(table2[i][3]), float(table2[i + 1][3]), 100, Func1)
    temp = temp - temp1
    s = abs(temp) + s

print("S заштрихованой части: ", s)
print()
print("Коды ошибок:")
print("0 - Нет ошибок")

print("1 - Превышение кол-во итераций")
print("2 - Корня нет на участке")
Draw(Func1, Func3)
