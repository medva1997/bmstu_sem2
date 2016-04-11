from tkinter import *
window=Tk()
window.title('Batton Example')
btn_end=Button(window,text='Exit', command=exit)

def tog():
    if(window.cget('bg')=='green'):
        window.configure(bg='yellow')
    else:
        if(window.cget('bg')=='yellow'):
            window.configure(bg='red')
        else:
            if(window.cget('bg')=='red'):
                window.configure(bg='purple')
            else:
                window.configure(bg='green')

btn_tog=Button(window,text='MAGGGIC',command=tog)
btn_end.pack(padx=150,pady=20)
btn_tog.pack(padx=150,pady=20,ipady=100)
window.mainloop()