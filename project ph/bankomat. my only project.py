from tkinter import *
root= Tk()
def func1 (ven):
    s=ent.get()
    if s== "1234":
        lb1.destroy()
        ent.destroy()
        but1=Button(fr1, bg="red",ent1= Entry(fr1, width=20, bg="yellow")
    ent1.pack()
    ent1.bind('<Return>', func4)
def func4 (ven):
    lb4= Label(fr1, width=40, bg="yellow", text="ВВедіть суму поповнення")
    lb4.pack()
    ent2= Entry(fr1, width=20, bg="yellow")
    sum=ent2.get()
    ent2.pack()
    ent2.bind('<Return>', func5)
def func5 (ven):
    lb5= Label(fr1, width=40, bg="yellow", text="Карту поповнено")
    lb5.pack()
fr1= Frame(root, bg="purple", bd=80)
lb1=Label(fr1, bg='red', text= "Пін- код", font="Arial 10")
lb1.grid(padx= 30, pady=1)
ent= Entry(fr1, width=20, bg="white")
ent.grid(row=0, column= 1, padx= 30, pady=20)
ent.bind('<Return>', func1)
fr1.pack()
root.mainloop()
