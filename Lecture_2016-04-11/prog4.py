from tkinter import *
import tkinter.messagebox as box
window=Tk()
window.title("Radio But")

frame=Frame(window)
book=StringVar()
radio_1=Radiobutton(frame,text='Mark 1',variable=book,value='1952')
radio_2=Radiobutton(frame,text='Pascal',variable=book,value='1970')
radio_3=Radiobutton(frame,text='C',variable=book,value='1972')
radio_4=Radiobutton(frame,text='C++',variable=book,value='1983')
radio_5=Radiobutton(frame,text='Java',variable=book,value='1995')

radio_1.select()

def dialog():
    box.showinfo('Selection','Chose lang: '+book.get())

btn=Button(frame,text='choose',command=dialog)
btn.pack(side=RIGHT)
radio_1.pack(side=LEFT)
radio_2.pack(side=LEFT)
radio_3.pack(side=LEFT)
radio_4.pack(side=LEFT)
radio_5.pack(side=LEFT)

frame.pack(padx=50,pady=50)
window.mainloop()