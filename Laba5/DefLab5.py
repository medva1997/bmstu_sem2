from tkinter import *
from math import *
from  random import *
root = Tk()
sgl = 1

def sun(x, y, radius):
    for i in range(0, 180, 10):
        rnd = randint(-5, 5)
        rx = (radius + rnd) * sin(i)
        ry = (radius + rnd) * cos(i)
        canv.create_line(x - rx, y - ry, x + rx, y + ry, width=2, fill='yellow')

def roket():
    canv.create_polygon(150,500, 170,300, 250,100, 330,300, 350,500, 300,500, 250,500, 200,500, 150,500, smooth=sgl, fill='white' )

    canv.create_oval(230,250,270,290, fill='lightblue' )
    x=290
    y=250
    k=20
    cl='yellow'
    canv.create_text(x, y+1*k, text='М', font="Verdana 14", anchor='w',justify=CENTER, fill=cl)
    canv.create_text(x, y+2*k, text='е', font="Verdana 14", anchor='w', justify=CENTER, fill=cl)
    canv.create_text(x, y+3*k, text='д', font="Verdana 14", anchor='w', justify=CENTER, fill=cl)
    canv.create_text(x, y+4*k, text='в', font="Verdana 14", anchor='w', justify=CENTER, fill=cl)
    canv.create_text(x, y+5*k, text='е', font="Verdana 14", anchor='w',justify=CENTER, fill=cl)
    canv.create_text(x, y+6*k, text='д', font="Verdana 14", anchor='w', justify=CENTER,fill=cl)
    canv.create_text(x, y+7*k, text='е', font="Verdana 14", anchor='w', justify=CENTER, fill=cl)
    canv.create_text(x, y+8*k, text='в', font="Verdana 14", anchor='w', justify=CENTER, fill=cl)
    z=15
    canv.create_polygon(180,500-z, 120,650-z, 180,600-z,  240,680-z,   280,680-z,  330,600-z,  390,650-z, 330, 500-z,350,500, 300,500, 250,500, 200,500, 150,500,smooth=sgl,fill='yellow')


    canv.create_polygon(177, 300, 120, 550, 180, 500, fill='red')
    canv.create_polygon(320, 300, 390, 550, 330, 500, fill='red')

    canv.create_polygon(220, 500, 250,430, 280, 500, 250,530,fill='green')




canv = Canvas(root, width=500, height=700, bg='lightblue', cursor='pencil')

canv.create_oval(-500,400,1000,800,fill='green')
roket()
sun(100,100,3)
sun(200,150,3)
sun(300,80,3)
sun(400,150,3)




canv.pack()
root.mainloop()
