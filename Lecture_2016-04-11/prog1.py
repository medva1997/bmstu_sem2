#   metod   buttons
#showinfo   OK
#showwarning    OK
# showerror     Ok
#askquestion Yes No
#askcancel   OK(return 1) and Cancel
#askyesno    Yes(return 1) and No
#askretrycansel Retry(return 1 ) and Cancel

from tkinter import *
import tkinter.messagebox as box
window=Tk()
window.title("Вывод сообщения")

def dialog():
    variant=box.askyesno("Блок сообщения"," Продолжать")
    if variant==1:
        box.showinfo("Блок Да","Продолжение")
    else:
        box.showwarning("Блок Нет","Выход")

btn=Button(window,text='Нажать', command=dialog())
btn.pack(padx=50, pady=50)
window.mainloop()