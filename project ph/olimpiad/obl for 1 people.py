from tkinter import *
from tkinter import messagebox
tk=Tk()
var1=IntVar()



def display(event):
    s="One people have "
    v=var1.get()
    if v==0:
        n=409.07/966400
    if v==1:
        n=839/2000884
    if v==2:
        n=350/1000419
    s+=str(n)+" "+"km^2"
    messagebox.showinfo("info", s)



var1.set(1)

rdk=Radiobutton(tk, variable=var1, value=0, text="Kropivnitskiy")
rdk.pack()

rdk2=Radiobutton(tk, variable=var1, value=1, text="Odessa")
rdk2.pack()

rdk3=Radiobutton(tk, variable=var1, value=2, text="Kiev")
rdk3.pack()

btn=Button(tk, text="Check")
btn.pack()

btn.bind("<Button-1>", display)
