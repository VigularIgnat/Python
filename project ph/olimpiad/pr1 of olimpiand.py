from tkinter import *

tk=Tk()
r=""
def func1():
    global r
    y=t.get()
    y=int(y)
    if y%4==0 and y%100!=0:
        r="Leap Year"
    else:
        r="Normal"
    lbl2["text"]=r
    
    
t=StringVar()

lbl=Label(tk, text="Check your year is big or not")
lbl.pack()

ent=Entry(tk, width=10, textvariable=t)
ent.pack()

btn=Button(tk, text="Check", command=func1)
btn.pack()

lbl2=Label(tk, text=r)
lbl2.pack()
