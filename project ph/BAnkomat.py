from tkinter import *
root= Tk()
def func(ven):
    s= ent.get()
    if s=="3333":
        lb1.destroy()
        ent.destroy()
        but= Button(root, bg='red', text='Balance')
        but.pack()
        but.bind('<Button-1>', func2)
    else:
        lb1.configure(text='not right kod. End.')
def func2(ven):
    lb2=Label(root, width =40, bg= 'yellow', text='on your balance 2000 ghrn')
    lb2.pack()
lb1= Label(root, bg= 'red', text= 'Пін код', font='Arial 10')
lb1.grid(padx=30, pady=1)
ent= Entry(root, width=20, bg='yellow')
ent.grid(row=0, column=1, padx= 5, pady=20)
ent.bind('<Return>', func)
root.mainloop()


