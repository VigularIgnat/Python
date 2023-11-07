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
    lb2=Label(root, width=40, bg= 'yellow',text='On your balance 3000 ghrn')
    butp= Button(root, bg='green', text='Bring money for your card')
    lb2.pack()
    butp.pack()
    butp.bind('<Button-2>', func3)
def func3(ven):
    name= ent3.get()
    if name =="Ignat":
     ent3.destroy()
      
lb1= Label(root, bg= 'red', text= 'Пін код', font='Arial 10')
lb1.grid(padx=30, pady=1)
ent= Entry(root, width=20, bg='yellow')
ent.grid(row=0, column=5, padx= 5, pady=20)
ent.bind('<Return>', func)
ent3= Entry(root, width=20, bg='purple')
ent3.grid(row=0, column=9, padx= 5, pady=20)
ent3.bind('<Return>', func)
root.mainloop()
