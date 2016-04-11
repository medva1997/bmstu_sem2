from tkinter import *
import tkinter.messagebox as box
window=Tk()

frame=Frame(window)
listbox=Listbox(frame)
listbox.insert(1,"Python")
listbox.insert(2,"Java")
listbox.insert(3,"Ada")
listbox.insert(4,"Delphi")
listbox.insert(5,"C")

def dialog():
    box.showinfo("Список для выбора",'Ваш выбор языка:'+listbox.get(listbox.curselection()))

btn=Button(frame,text="Выбор",command=dialog)
btn.pack(side=RIGHT,padx=10)
listbox.pack(side=LEFT)
frame.pack(padx=50, pady=50)
window.mainloop()
