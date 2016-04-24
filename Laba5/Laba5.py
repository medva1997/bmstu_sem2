from tkinter import *
from math import *
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
    points.append([xleft, ydown])
    points.append([xleft, ydown - hightleft])
    points.append([(xleft + xright) / 2, ydown - hightleft])
    points.append([(xleft + xright) / 2, ydown - hightright])
    points.append([xright, ydown - hightright])
    points.append([xright, ydown])

    canv.create_polygon(points)


canv = Canvas(root, width=1000, height=500, bg='lightblue', cursor='pencil')
# canv.create_line(200, 50, 300, 50, width=3, fill='blue')


whell_y = 200
whell_radius = 30
whell_distandce = 4
first_whell_x = 100
second_whell_x = 300

cabine_front_x = first_whell_x - whell_radius - whell_distandce
cabine_back_x = second_whell_x + 3 * whell_radius + 2 * whell_distandce
cabine_down_y = whell_y

cabine(cabine_front_x, cabine_down_y, cabine_back_x, 150, 50)

whell(first_whell_x, whell_y, whell_radius)
backwhell(second_whell_x, whell_y, whell_radius, whell_distandce)
backwhell(650, whell_y, whell_radius, whell_distandce)
canv.pack()
root.mainloop()
