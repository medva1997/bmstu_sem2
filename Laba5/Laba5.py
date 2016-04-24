from tkinter import *

root = Tk()

canv = Canvas(root, width=500, height=500, bg='lightblue', cursor='pencil')
canv.create_line(200, 50, 300, 50, width=3, fill='blue')
canv.pack()
root.mainloop()
