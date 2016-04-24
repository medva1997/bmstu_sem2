from tkinter import *
from math import *
from  random import *
root = Tk()


# Draw whell with lines
def whell(x, y, radius):
    canv.create_oval(x - radius, y - radius, x + radius, y + radius, width=3, fill='white')
    r = radius / sqrt(2)
    canv.create_line(x - r, y - r, x + r, y + r, width=2, fill='blue')
    canv.create_line(x + r, y - r, x - r, y + r, width=2, fill='blue')


# Draw back pair of whell
def backwhell(x, y, radius, distance):
    whell(x, y, radius)
    whell(x + distance + 2 * radius, y, radius)


def cabine(xleft, ydown, xright, hightleft, hightright):
    points = []
    # cabine
    xmiddle = (xleft + xright) / 2
    points.append([xleft, ydown])
    points.append([xleft, ydown - hightleft])
    points.append([xmiddle, ydown - hightleft])
    points.append([xmiddle, ydown - hightright])
    points.append([xright, ydown - hightright])
    points.append([xright, ydown])
    canv.create_polygon(points, fill='red')

    # cabine connector
    points = []
    points.append([xmiddle + (xright - xmiddle) // 4, ydown - hightright - (hightleft - hightright) * 1 / 6])
    points.append([xmiddle + (xright - xmiddle) // 3 * 2, ydown - hightright])
    canv.create_rectangle(points, fill='red')
    return points[0][1]


def trailer(xleft, ydown, xright, connecter_y, hightright, xdownleft):
    points = []
    points.append([xleft, connecter_y])
    points.append([xleft, ydown - hightright])
    points.append([xright, ydown - hightright])
    points.append([xright, ydown])

    points.append([xdownleft, ydown])
    points.append([xdownleft, connecter_y])

    canv.create_polygon(points, fill='yellow')


def sun(x, y, radius):
    for i in range(0, 180, 10):
        rnd = randint(-5, 5)
        rx = (radius + rnd) * sin(i)
        ry = (radius + rnd) * cos(i)
        canv.create_line(x - rx, y - ry, x + rx, y + ry, width=2, fill='yellow')


def cloud(x, y, radius):
    for i in range(15):
        rndx = randint(x - radius, x + radius)
        rndy = randint(y - radius // 3, y + radius // 3)
        k = randint(30, 70) / 100
        canv.create_oval(rndx - radius, rndy - radius * k, rndx + radius, rndy + radius * k, width=0, fill='blue')


def tree(x, y, higth, width, n):
    canv.create_rectangle(x - 1 / 2 * width, y + 15, x + 1 / 2 * width, y - higth / 2, fill='brown')
    for i in range(2 * n):
        yk = y - higth / (2 * n) * i
        canv.create_polygon(x - 1 / 2 * width * (2 * n - i), yk, x + 1 / 2 * width * (2 * n - i), yk, x, yk - higth / n,
                            fill='green')




canv = Canvas(root, width=1000, height=500, bg='lightblue', cursor='pencil')
# canv.create_line(200, 50, 300, 50, width=3, fill='blue')


whell_y = 400
whell_radius = 30
whell_distandce = 4

first_whell_x = 100
second_whell_x = 300
back_whell_x = 650

cabine_front_higth = 150
cabine_back_higth =50

cabine_front_x = first_whell_x - whell_radius - whell_distandce
cabine_back_x = second_whell_x + 3 * whell_radius + 2 * whell_distandce
cabine_down_y = whell_y

xmiddle = (cabine_front_x + cabine_back_x) / 2
trailer_front_x = xmiddle + (cabine_back_x - xmiddle) // 8
trailer_down_y = cabine_down_y
trailer_back_x = back_whell_x + 3 * whell_radius + 2 * whell_distandce
trailer_back_hight = cabine_front_higth

connecter_y = cabine(cabine_front_x, cabine_down_y, cabine_back_x, cabine_front_higth, cabine_back_higth)
trailer(trailer_front_x, trailer_down_y, trailer_back_x, connecter_y, trailer_back_hight, cabine_back_x + 10)

whell(first_whell_x, whell_y, whell_radius)
backwhell(second_whell_x, whell_y, whell_radius, whell_distandce)
backwhell(back_whell_x, whell_y, whell_radius, whell_distandce)

sun(100, 100, 50)
cloud(600, 100, 50)

tree(900, whell_y + whell_radius, 200, 10, 8)
canv.pack()
root.mainloop()
