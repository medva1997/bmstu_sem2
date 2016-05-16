from tkinter import *
import tkinter.messagebox as box


def dialog():
    variant = box.askyesno("Блок сообщения", " Продолжать")
    if variant == 1:
        box.showinfo("Блок Да", "Продолжение")
    else:
        box.showwarning("Блок Нет", "Выход")


def dialog2():
    box.showinfo("Приглашение", "Сдавать экзамен в сентябре " + entry.get())


window = Tk()
window.title('PК')
frame = Frame(window)
entry = Entry(frame)

label2 = LabelFrame(window, text='openform2')
label2.pack(padx=150, pady=20)
btn = Button(frame, text='Введите фамилию', command=dialog2)
label = Label(label2, text='openform')
btn_end = Button(window, text='Exit', command=exit)
btn_tog = Button(window, text='openform', command=dialog)
btn_end.pack(padx=150, pady=20)
btn.pack(side=RIGHT, padx=10)
entry.pack(side=LEFT)
frame.pack(padx=50, pady=50)
btn_tog.pack(padx=150, pady=20, ipady=50)
label.pack()

window.mainloop()
