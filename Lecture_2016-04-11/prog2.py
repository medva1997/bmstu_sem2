"Ввод данных. Сцществует односточное поле для ввода текста."
from tkinter import *
import tkinter.messagebox as box


window=Tk()
window.title("Виджет Entry")

frame=Frame(window)
entry=Entry(frame)

def dialog():
    box.showinfo("Приглашение","Сдавать экзамен в сентябре "+entry.get())


btn = Button(frame, text='Введите фамилию', command=dialog)
btn.pack(side=RIGHT,padx=10)
entry.pack(side=LEFT)
frame.pack(padx=50, pady=50)
window.mainloop()
